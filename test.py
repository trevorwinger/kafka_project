from consumer import Consumer
from producer import Producer

def make_messages(num_messages, message_txt):
    messages = []
    for i in range(num_messages):
        messages.append(message_txt + str(i))
    return messages


def main():
    topic = 'test'
    servers = ['localhost:9092']
    group_id = 'test_group'
    message = 'test message'
    num_messages = 100

    producer = Producer(topic, servers)
    for m in make_messages(num_messages, message):
        producer.produce(m)
    #producer.async_produce(make_messages(num_messages, message))
    producer.close()

    consumer = Consumer(topic, group_id, servers)
    consumer.consume()
    consumer.close()

if __name__ == '__main__':
    main()
