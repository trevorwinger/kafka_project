from kafka import KafkaProducer
from kafka.errors import KafkaError


class Producer:
    def __init__(self, topic, servers):
        self.kp = KafkaProducer(bootstrap_servers=servers, retries=5, api_version=(0,11,5))
        self.topic = topic

    def produce(self, message):
        try:
            temp = self.kp.send(self.topic, bytes(message, 'utf-8'))
            #can access metadata here by doing temp.get()
            #commented out because it makes the output messy
            #print('temp', temp.get())
        except KafkaError as e:
            print(e)

    def async_produce(self, messages):
        for message in messages:
            print('message', message)
            self.produce(message)
        #send all messages first
        self.kp.flush()
        #then close the producer
        print('Done producing')
        self.close()

    def close(self):
        self.kp.close()