import json
import pika

from app import Product, db


amqp = "amqp://user:password@rabbit:5672/jango-flask"
# amqp = "amqps://ftvpsxry:YSuyDjGGTEoU-0xhoWMlJ2RxcZbnYIrU@cougar.rmq.cloudamqp.com/ftvpsxry"
params = pika.URLParameters(amqp)
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(channel, method, properties, body):
    print('Recieved in main')
    data = json.loads(body)
    print(channel)
    print(data)
    print(method)
    print(properties.content_type)
    if properties.content_type == "product_created":
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()
        print('Product created')
    elif properties.content_type == "product_updated":
        print('product_updated in main')
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()
        print('Product Updated')
    elif properties.content_type == "product_deleted":
        product = Product.query.get(data['id'])
        db.session.delete(product)
        db.session.commit()
        print('Product deleted')


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()

# import os
# import pika

# # Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
# url = 'amqp://user:password@rabbit:5672/jango-flask'
# params = pika.URLParameters(url)
# connection = pika.BlockingConnection(params)
# channel = connection.channel()  # start a channel
# channel.queue_declare(queue='main')  # Declare a queue


# def callback(ch, method, properties, body):
#     print(" [main] Received " + str(body))
#     print(ch)
#     print('\n')
#     print(method)
#     print('\n')
#     print(properties)


# channel.basic_consume('main',
#                       callback,
#                       auto_ack=True)

# print(' [main] Waiting for messages:')
# channel.start_consuming()
# channel.close()
# connection.close()
