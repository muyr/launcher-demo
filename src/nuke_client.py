#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = 'andyguo'

import threading
import pika
import json
import random


class NukeClient(threading.Thread):
    response_body = {'status': 'ok',
                     'error_code': 1000,
                     'message': 'successful',
                     'data': []}

    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters())
        self.channel = self.connection.channel()
        self.channel.basic_qos(prefetch_count=1)

        self.consume_queue = self.channel.queue_declare(queue='electron.nuke').method.queue

        self.channel.basic_consume(consumer_callback=self.on_request,
                                   queue='electron.nuke',
                                   no_ack=True)

    def on_request(self, channel, method, properties, body):
        print body
        import time
        time.sleep(1)
        body = json.loads(body)
        # print body
        result = random.choice([('ok', u'成功创建节点 Blur1'), ('error', u'创建失败')])
        channel.basic_publish(exchange='',
                              routing_key=properties.reply_to,
                              properties=pika.BasicProperties(correlation_id=properties.correlation_id),
                              body=json.dumps({'status': result[0],
                                               'error_code': 1000,
                                               'message': result[1],
                                               'data': []}))
        # self.channel.basic_ack(delivery_tag=method.delivery_tag)

    def start(self):
        self.channel.start_consuming()


if __name__ == '__main__':
    client = NukeClient()
    client.start()
