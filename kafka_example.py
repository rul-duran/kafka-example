from kafka import KafkaProducer, KafkaConsumer
import json
import time

TOPIC = "example_topic"

def produce_messages():
    producer = KafkaProducer(
        bootstrap_servers="localhost:9092",
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    for i in range(10):
        message = {"id": i, "message": f"Message {i}"}
        producer.send(TOPIC, message)
        print(f"Produced: {message}")
        time.sleep(1)
    producer.close()

def consume_messages():
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers="localhost:9092",
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="example-group",
        value_deserializer=lambda v: json.loads(v.decode("utf-8"))
    )
    for message in consumer:
        print(f"Consumed: {message.value}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Kafka Example")
    parser.add_argument("--mode", choices=["producer", "consumer"], required=True, help="Run as producer or consumer")
    args = parser.parse_args()

    if args.mode == "producer":
        produce_messages()
    elif args.mode == "consumer":
        consume_messages()
