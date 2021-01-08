#coding=utf-8

from time import sleep
import threading
import paho.mqtt.client as mqtt
import random
import IP_Functions
import config

# ------------------------------------------------------------------------
# mqtt callback functions
# ------------------------------------------------------------------------
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

# ------------------------------------------------------------------------
# QUBE_MQTT_CtrlLogic
# ------------------------------------------------------------------------

def Mqtt_Working_Thread():

    MqttServerConf = config.loadMqttConfiguration('config/MqttIPReporter.ini')
    RateConf = config.loadRateConfiguration('config/MqttIPReporter.ini')
    TopicConf = config.loadTopicConfiguration('config/MqttIPReporter.ini')

    while(True):
        ClientID = TopicConf['root'] + "/" + str(random.random()*10000)
        client = mqtt.Client(ClientID)
        client.on_connect = on_connect
        client.on_message = on_message
        client.username_pw_set(MqttServerConf['username'],MqttServerConf['passwd'])
        client.connect(MqttServerConf['ip'], int(MqttServerConf['port']), 60)

        # 启动 mqtt client
        client.loop_start()

        threadRunning = True

        while(threadRunning):
            try:
                hostname = IP_Functions.get_host_name()
                IP = IP_Functions.get_host_ip()
                client.publish(TopicConf['root'] + "/" + hostname + "/IP", IP)
                print(hostname + " : " + IP)
                # Report IP every `RateConf['publish']` seconds
                sleep(float(RateConf['publish']))
                pass
            except expression as identifier:
                threadRunning = False
                print(identifier)
                pass


        # 停止 mqtt client
        client.loop_stop()

        # Reconnect Timeout = `RateConf['reconnect']`
        sleep(float(RateConf['reconnect']))


if __name__ == '__main__':
    Mqtt_Working_Thread()
