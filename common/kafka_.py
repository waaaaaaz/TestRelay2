# coding: utf-8

from kafka import KafkaProducer
import json


class KAFKALibrary(object):

    def __init__(self, kafka_host, kafka_topic):
        self.kafka_host = kafka_host
        self.kafka_topic = kafka_topic
        self.producer = KafkaProducer(bootstrap_servers=self.kafka_host)

    def produce(self, message):
        print(message)
        self.producer.send(self.kafka_topic, json.dumps(message).encode('utf-8'))
        self.producer.flush()