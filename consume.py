import pulsar
import os
import time

protocol_url = os.getenv('PROTOCOL_URL', 'pulsar://localhost:6650')


def main():
    client = pulsar.Client(protocol_url)
    consumer = client.subscribe('my-topicc', 'my-subscription')

    consumer_routine(consumer)
    client.close()

def consumer_routine(consumer):
    while True:
        msg = consumer.receive()
        print("Received message '{}' id='{}'".format(msg.data(), msg.message_id()))
        consumer.acknowledge(msg)
        #time.sleep(2)
    except KeyboardInterrupt:
        print('interrupted!')


main()
