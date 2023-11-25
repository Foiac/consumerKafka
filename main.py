from infrastructure.messaging.consumerkafka import consumerkafka

class main():

    if __name__ == "__main__":

        kafka_consumer = consumerkafka('localhost:9093', 'Post.Sale') 
        kafka_consumer.readKafka()

main()