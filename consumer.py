from kafka import KafkaConsumer

class Consumer:
    def __init__(self, topic, group_id, servers):
        self.kc = KafkaConsumer(topic, group_id=group_id, bootstrap_servers=servers)

    def consume(self):
        count = 0
        for message in self.kc:
            '''
            Here is where you could do some processing with the consumer; 
            for example, you could write the message to a file.

            Data values are as follows:
            message.topic: topic name
            message.partition: partition number
            message.offset: offset number
            message.key: key
            message.value: value
            '''
            print(message)
            self.write_to_file('./files/' +'test' + str(count) + '.txt', message.value.decode('utf-8'))
            count += 1
    
    def write_to_file(self, filename, message):
        with open(filename, 'a') as f:
            f.write(message)

    def close(self):
        self.kc.close()

