# your-first-dockerfile

![Docker Image CI](https://github.com/supernevstop/MqttIPReporter/workflows/Docker%20Image%20CI/badge.svg)

## BUILD DOCKER IMAGE

```
docker build . -t mqtt_ip_reporter:latest
```

## STARTUP A REPORTER CONTAINER

```
docker run -d --restart always --network host --name mqtt_ip_reporter mqtt_ip_reporter:latest
```
