import pika
import json

amqp = "amqp://user:password@rabbit:5672/jango-flask"
# amqp = "amqps://ftvpsxry:YSuyDjGGTEoU-0xhoWMlJ2RxcZbnYIrU@cougar.rmq.cloudamqp.com/ftvpsxry"
params = pika.URLParameters(amqp)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    props = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=props)
    print(props)

# import pika
# import os



# # Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
# amqp = 'amqp://user:password@rabbit:5672/jango-flask'
# # amqp = 'amqp://user:password@localhost:5672/jango-flask'
# # amqp = "amqps://ftvpsxry:YSuyDjGGTEoU-0xhoWMlJ2RxcZbnYIrU@cougar.rmq.cloudamqp.com/ftvpsxry"

# params = pika.URLParameters(amqp)
# connection = pika.BlockingConnection(params)
# channel = connection.channel()  # start a channel
# props = pika.BasicProperties('property!')
# channel.basic_publish(exchange='',
#                       routing_key='admin',
#                       body='Hello CloudAMQP!',
#                       properties=props)

# print(" [main] Sent 'Hello World! admin'")
# channel.close()
# connection.close()
