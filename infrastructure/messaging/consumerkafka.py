from kafka import KafkaConsumer
from json import loads

class consumerkafka:
    ''' This application able read data from kafka broker 

     Keyword Arguments:
        server: kafka connection host 
        topic: kafka topic'''
    
    def __init__(self, server, topic):
        self.server = server
        self.topic = topic

        self.consumer = KafkaConsumer(self.topic,
                            bootstrap_servers=self.server,
                            auto_offset_reset='earliest',
                            enable_auto_commit=True,
                            group_id='my-group')

    def readKafka(self):
        for message in self.consumer:
            read = loads(message.value.decode('utf-8'))
            try:
                print("Mensagem recebida: " + read['mensagem'])
            except:
                print("Aguardando mensagens")