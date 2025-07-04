import paho.mqtt.client as mqtt
from config.config import MQTT_HOST, MQTT_PORT, MQTT_TOPIC
from backend.utils.logger import logger

def run_subscriber(message_handler):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            logger.info("Połączono z MQTT")
            client.subscribe(MQTT_TOPIC)
        else:
            logger.error("błąd połączenia error: {rc}")

    def on_message(client, userdata, msg):
        payload = msg.payload.decode()
        logger.info(f"Otrzymano wiadomość:{payload}")
        message_handler(payload)

        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message

        client.connect(MQTT_HOST, MQTT_PORT, keepalive=60)
        client.loop_forever()
