#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = 'andyguo'

import pika
import uuid
import json


class ElectronServer(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters())
        self.channel = self.connection.channel()

        self.request_queue = self.channel.queue_declare(queue='electron.nuke').method.queue
        self.response_queue = self.channel.queue_declare(exclusive=True).method.queue

        self.channel.basic_consume(consumer_callback=self.on_response,
                                   queue=self.response_queue)
        self.correlation_id = None

    def on_response(self, channel, method, properties, body):
        if self.correlation_id == properties.correlation_id:
            self.response = json.loads(body)

    def request(self, body):
        self.response = None
        self.correlation_id = str(uuid.uuid4().hex)

        self.channel.basic_publish(exchange='',
                                   routing_key='electron.nuke',
                                   properties=pika.BasicProperties(reply_to=self.response_queue,
                                                                   correlation_id=self.correlation_id),
                                   body=json.dumps(body))

        while self.response is None:
            self.connection.process_data_events(0.5)

        return self.response


if __name__ == '__main__':
    server = ElectronServer()

    message = {'url' : '/nuke/create',
               'body': [{'key': 'value'}]}

    print server.request(json.dumps(message))
