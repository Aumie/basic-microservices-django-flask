FROM python:3.9
#to see logs in real-time
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt


RUN pip install -r requirements.txt
COPY . /app
