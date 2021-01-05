# Mqtt_IP_Reporter

![Docker Image CI](https://github.com/supernevstop/MqttIPReporter/workflows/Docker%20Image%20CI/badge.svg)


## STARTUP A REPORTER CONTAINER

```
docker build . -t mqtt_ip_reporter:latest
docker run -d --restart always --network host --name mqtt_ip_reporter mqtt_ip_reporter:latest
```

OR you can use the dockerhub image directly.

```
docker run -d --restart always --network host --name mqtt_ip_reporter nevstop/mqtt_ip_reporter:latest
```
