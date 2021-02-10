# Python Pulsar Test

To test you'll need to boot the pulsar broker service, the consumer, which will occupy a terminal, and a producer which will occupy a second terminal and recieve `enter` keystrokes.

```
$ docker-compose build python_pulsar_producer
$ docker-compose up -d standalone

# Terminal 1
$ docker-compose up python_pulsar_consumer

# Terminal 2 which is interactive (hit enter to send messages)
$  docker-compose up -d python_pulsar_producer && docker attach pulsar-latency-test_python_pulsar_producer_1
```
