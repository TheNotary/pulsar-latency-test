import pulsar
import os

protocol_url = os.getenv('PROTOCOL_URL', 'pulsar://localhost:6650')

topic_name = "my-topicc"
topic_name = "persistent://public/default/my-topicc"
n_messages = 10

def main():
    client = pulsar.Client(protocol_url)
    producer = client.create_producer(topic_name,
                                      block_if_queue_full=True,
                                      batching_enabled=True,
                                      batching_max_publish_delay_ms=10)

    producer_routine(producer)

    client.close()


def producer_routine(producer):
    print('Ready, press ENTER to send ' + str(n_messages) + ' to pulsar topic ' + topic_name)
    while input() != 'quit':
        print("writing to pulsar")
        for i in range(n_messages):
            producer.send(('Hello-%d' % i).encode('utf-8'))
        producer.flush()

main()
