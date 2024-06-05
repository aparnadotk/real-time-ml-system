from quixstreams import Application

def produce_trades(
        kafka_broker_address: str,
        kafka_topic_name: str
) -> None:
    """
    Reads trades in real-time from the Kraken Websocket API and writes them to a Kafka topic.

    Args:
        kafka_broker_address (str): The address of the Kafka broker.
        kafka_topic_name (str): The name of the Kafka topic.
    
    Returns: 
        None
    """
    
    app = Application(broker_address=kafka_broker_address)

    # Define the topic we will use to save the trades.
    topic = app.topic(name=kafka_topic_name, value_serializer='json')

    event = {"id": "1", "text": "Lorem ipsum dolor sit amet"}

    # Create a Producer instance
    with app.get_producer() as producer:
        while True:
            # Serialize an event using the defined Topic 
            message = topic.serialize(key=event["id"], value=event)

            # Produce a message into the Kafka topic
            producer.produce(
                topic=topic.name, value=message.value, key=message.key
            )
            print('Message sent')

            from time import sleep
            sleep(1)

if __name__ == '__main__':
    produce_trades(
        kafka_broker_address='localhost:19092', 
        kafka_topic_name='trade'
    )