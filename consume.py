import pulsar
import os
import time

protocol_url = os.getenv('PROTOCOL_URL', 'pulsar://localhost:6650')


def main():
    client = pulsar.Client(protocol_url)
    consumer = client.subscribe('my-topicc', 'my-subscription')

    try:
        consumer_routine(consumer)
    except KeyboardInterrupt:
        client.close()


def consumer_routine(consumer):
    while True:
        try:
            msg = consumer.receive(1000)
            print("Received message '{}' id='{}'".format(msg.data(), msg.message_id()))
            consumer.acknowledge(msg)
        except:
            continue


main()

