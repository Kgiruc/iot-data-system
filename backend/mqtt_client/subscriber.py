import paho.mqtt.client as mqtt
from config.config import MQTT_HOST, MQTT_PORT, MQTT_TOPIC
from utils.logger import logger

def run_subscriber(message_handler):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            logger.info("Połączono z MQTT")
            for topic in MQTT_TOPIC.values():
                client.subscribe(topic)
                logger.info(f"Zasubskrybowano: {topic}")
        else:
            logger.error(f"Błąd połączenia MQTT: {rc}")

    def on_message(client, userdata, msg):
        try:
            payload = msg.payload.decode()
            topic = msg.topic
            logger.info(f"Otrzymano wiadomość z tematu '{topic}': {payload}")
            message_handler(topic, payload)
        except Exception as e:
            logger.error(f"Błąd w on_message:{e}")

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_HOST, MQTT_PORT, keepalive=60)
    client.loop_forever()