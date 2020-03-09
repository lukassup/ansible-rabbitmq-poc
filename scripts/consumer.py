#!/usr/bin/env python
import os
import time

import pika

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT", "5672"))
RABBITMQ_VHOST = os.getenv("RABBITMQ_VHOST", "/conejo")
RABBITMQ_USERNAME = os.getenv("RABBITMQ_USERNAME", "conejo")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD", "conejo")


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b"."))
    print(" [x] Done")


if __name__ == "__main__":
    credentials = pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=RABBITMQ_HOST,
            port=RABBITMQ_PORT,
            virtual_host=RABBITMQ_VHOST,
            credentials=credentials,
        )
    )
    channel = connection.channel()
    channel.queue_declare(queue="hello")
    channel.basic_consume(queue="hello", auto_ack=True, on_message_callback=callback)
    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()
