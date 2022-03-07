from kafka import KafkaProducer
from kafka.errors import KafkaError


class Producer:
    def __init__(self, topic, servers):
        self.kp = KafkaProducer(bootstrap_servers=servers, retries=5)
        self.topic = topic

    def produce(self, message):
        try:
            temp = self.kp.send(self.topic, bytes(message, 'utf-8'))
        except KafkaError as e:
            print(e)

    def async_produce(self, messages):
        for message in messages:
            print('message', message)
            self.produce(message)
        #send all messages first
        self.kp.flush()

    def close(self):
        self.kp.close()