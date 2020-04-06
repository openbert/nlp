import json
import os

import pika
import spacy

print("Start read.py")

print("Connect to RabbitMQ...")
connection = pika.BlockingConnection(
    pika.connection.URLParameters(os.getenv('RABBITMQ_URL'))
)
channel = connection.channel()
channel.queue_declare(queue='ner_request')
channel.queue_declare(queue='ner_response')
print("ok")

print("Load spaCy model...")
nlp = spacy.load('de_core_news_md')
print("ok")


def callback(ch, method, properties, body):
    request = json.loads(body)
    print(request)
    doc = nlp(request["text"])
    response = {
        "source": request["source"],
        "sourceUuid": request["sourceUuid"],
        "entities": []
    }
    for ent in doc.ents:
        response["entities"].append({
            "name": ent.text,
            "label": ent.label_,
            "startChar": ent.start_char,
            "endChar": ent.end_char,
        })
    print(json.dumps(response))
    ch.basic_publish(
        exchange="",
        routing_key='ner_response',
        body=json.dumps(response),
        properties=pika.BasicProperties(
            delivery_mode=2
        )
    )
    # ch.basic_ack(delivery_tag=method.delivery_tag)


print("Start consume")
channel.basic_consume(queue='ner_request', auto_ack=True, on_message_callback=callback)
channel.start_consuming()
