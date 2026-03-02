import os
import django
import json
from kafka import KafkaConsumer
from users.tasks import send_welcome_email

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()


consumer = KafkaConsumer(
    "user_registered",
    bootstrap_servers="kafka:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    group_id="user-group",
    auto_offset_reset="earliest",
)

print("Kafka Consumer started...")

for message in consumer:
    data = message.value
    print("Received event:", data)
    send_welcome_email.delay(data["email"])