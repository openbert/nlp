import json
import os

import pika

connection = pika.BlockingConnection(
    pika.connection.URLParameters(os.getenv('RABBITMQ_URL'))
)
channel = connection.channel()
channel.queue_declare("ner_request")
channel.queue_declare("ner_response")

text = """
Das Historische Bürgerhaus Langenberg und die Vorburg von Schloss Hardenberg sind ohne Besucher, ohne Darsteller auf der Bühne, eben wie weitere unzählige öffentlichen Gebäuden in Zeiten der Corona-Krise - das ist ein seltsamer Zustand.

Die "Velberter Kulturloewen" arbeiten trotzdem hinter den Kulissen und haben sich gedacht: „Wenn unsere Besucher nicht zu uns kommen können, dann kommen wir eben zu ihnen!“ Und schon rauchten die kreativen Köpfe, um ein Programm zusammenzustellen, das sich „Kultur im Wohnzimmer“ nennt.
Ob im Radio, in der Presse oder auf ihren Social Media Kanälen, sie haben sich Einiges überlegt und freuen sich, auch in Zeiten der Veranstaltungsabsagen, Künstler zu unterstützen und ihnen eine Plattform für ihre Beiträge zu bieten. Zu hören und zu sehen gibt es ein vielfältiges Programm für Groß und Klein und dabei auch die Möglichkeit, selbst aktiv zu werden. Hier folgt der erste Aufschlag:
"""

payload = {
    "source": "lorem",
    "sourceUuid": "1234",
    "text": text
}

print("send test message")
channel.basic_publish(
    exchange="",
    routing_key="ner_request",
    body=json.dumps(payload),
    properties=pika.BasicProperties(delivery_mode=2)
)


def callback(ch, method, properties, body):
    print(json.loads(body))
    # ch.basic_ack(method.delivery_tag)


print("start consume")
channel.basic_consume(queue="ner_response", on_message_callback=callback, auto_ack=True)
channel.start_consuming()
