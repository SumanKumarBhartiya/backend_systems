from kafka import KafkaProducer
import json


def get_kafka_producer():

    return KafkaProducer(
        bootstrap_servers="kafka:9092",
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )


def send_welcome_email_kafka(email, name):

    producer = get_kafka_producer()

    producer.send("user_registered", {"email": email, "name": name})
    producer.flush()
    producer.close()
