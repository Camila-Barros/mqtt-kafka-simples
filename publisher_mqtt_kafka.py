import paho.mqtt.client as mqtt
from pykafka import KafkaClient
from random import uniform
import time

mqtt_broker = 'mqtt.eclipseprojects.io'
mqtt_client = mqtt.Client('MQTTProducer')
mqtt_client.connect(mqtt_broker)

kafka_client = KafkaClient(hosts='localhost:9092')
kafka_topic = kafka_client.topics['temperatura']
kafka_producer = kafka_topic.get_sync_producer()

while True:
    randNumber = uniform(24.0, 26.0)
    mqtt_client.publish("temperatura", randNumber)
    print('MQTT: publicou ' + str(randNumber) + ' no tópico TEMPERATURA')

    kafka_producer.produce(str(randNumber).encode('ascii'))
    print('KAFKA: publicou ' + str(randNumber) + ' no tópico TEMPERATURA')
    time.sleep(5)
