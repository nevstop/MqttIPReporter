#coding=utf-8

import configparser
import os
import sys

def loadMqttConfiguration(filepath):

    if(os.path.isabs(filepath) == False):
        filepath = os.path.join(sys.path[0],filepath)

    print(filepath)

    config = configparser.ConfigParser()
    if(os.path.exists(filepath) == False):
        config.add_section('mqtt')
        config.set( 'mqtt', 'ip', 'mqtt.iecube.com.cn')
        config.set( 'mqtt', 'port', '1883')
        config.set( 'mqtt', 'username', '')
        config.set( 'mqtt', 'passwd', '')
        with open(filepath, 'w', encoding='utf-8') as file:
            config.write(file)  # 值写入配置文件

    config.read(filepath, encoding='UTF-8')
    # print(config['mqtt']['ip'])
    # print(config['mqtt']['port'])
    # print(config['mqtt']['username'])
    # print(config['mqtt']['passwd'])

    return {'ip':config['mqtt']['ip'],
            'port':config['mqtt']['port'],
            'username':config['mqtt']['username'],
            'passwd':config['mqtt']['passwd']}

if __name__ == '__main__':
    print(loadMqttConfiguration('config/MqttIPReporter.ini'))