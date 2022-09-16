import pika
import json

amqp = "amqp://user:password@rabbit:5672/jango-flask"
# amqp = "amqps://ftvpsxry:YSuyDjGGTEoU-0xhoWMlJ2RxcZbnYIrU@cougar.rmq.cloudamqp.com/ftvpsxry"
params = pika.URLParameters(amqp)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    props = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=props)
    print(props)

# import pika
# import os


# def pubish(method, body):
#     pass
# # Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
# url = 'amqp://user:password@rabbit:5672/jango-flask'
# params = pika.URLParameters(url)
# connection = pika.BlockingConnection(params)
# channel = connection.channel()  # start a channel
# props = pika.BasicProperties('property!')
# channel.basic_publish(exchange='',
#                       routing_key='main',
#                       body='Hello CloudAMQP!main',
#                       properties=props)

# print(" [admin] Sent 'Hello World!'")
# channel.close()
# connection.close()
