#!/usr/bin/env python
import os
import sys

import pika

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT", "5672"))
RABBITMQ_VHOST = os.getenv("RABBITMQ_VHOST", "/conejo")
RABBITMQ_USERNAME = os.getenv("RABBITMQ_USERNAME", "conejo")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD", "conejo")

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
    channel.queue_declare(queue="task_queue", durable=True)
    message = " ".join(sys.argv[1:]) or "Hello World!"
    channel.basic_publish(
        exchange="",
        routing_key="task_queue",
        body=message,
        properties=pika.BasicProperties(delivery_mode=2),
    )
    print(" [x] Sent %r" % message)
    connection.close()
