FROM rabbitmq:3-management
#to see logs in real-time

ENV RABBITMQ_DEFAULT_USER user
ENV RABBITMQ_DEFAULT_PASS password
ENV RABBITMQ_DEFAULT_VHOST jango-flask

# doesn't have curl by default
RUN apt-get update
RUN apt-get -y install curl

