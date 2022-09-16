import pika
import json
import django
from django.conf import settings
from admin import settings as admin_settings
import os
# os.environ['DJANGO_SETTINGS_MODULE'] = "admin.settings"
settings.configure(DEBUG=admin_settings.DEBUG, DATABASES=admin_settings.DATABASES)
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()
from products.models import Product    # nopep8

# set this bc this file is outside of django project

amqp = "amqp://user:password@rabbit:5672/jango-flask"
# amqp = "amqps://ftvpsxry:YSuyDjGGTEoU-0xhoWMlJ2RxcZbnYIrU@cougar.rmq.cloudamqp.com/ftvpsxry"

params = pika.URLParameters(amqp)
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Recieved in admin')
    data = json.loads(body)
    print(data)
    print(properties.content_type)
    # print(type(data['user_id']))
    product = Product.objects.get(id=data['product_id'])
    if properties.content_type == "product_like_add":
        product.likes = product.likes + 1
        product.save()
        print('Product likes increased')
    elif properties.content_type == "product_like_remove":
        product.likes = product.likes - 1
        product.save()
        print('Product likes decreased')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()


# import pika
# import os

# # Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
# amqp = 'amqp://user:password@rabbit:5672/jango-flask'
# # amqp = 'amqp://user:password@localhost:5672/jango-flask'
# # amqp = "amqps://ftvpsxry:YSuyDjGGTEoU-0xhoWMlJ2RxcZbnYIrU@cougar.rmq.cloudamqp.com/ftvpsxry"

# params = pika.URLParameters(amqp)
# connection = pika.BlockingConnection(params)
# channel = connection.channel()  # start a channel
# channel.queue_declare(queue='admin')  # Declare a queue


# def callback(ch, method, properties, body):
#     print(" [admin] Received " + str(body))
#     print(ch)
#     print('\n')
#     print(method)
#     print('\n')
#     print(properties)


# channel.basic_consume('admin',
#                       callback,
#                       auto_ack=True)

# print(' [admin] Waiting for messages:')
# channel.start_consuming()
# channel.close()
# connection.close()
