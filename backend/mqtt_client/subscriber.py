import paho.mqtt.client as mqtt
from config.config import MQTT_HOST, MQTT_PORT, MQTT_TOPIC

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Połączono z MQTT brokerem!")
        client.subscribe(MQTT_TOPIC)
        print(f"Subskrybowano temat: {MQTT_TOPIC}")
    else:
        print("Błąd połączenia z brokerem. Kod:", rc)

def on_message(client, userdata, msg):
    print("📨 Otrzymano wiadomość:")
    print(f"Topic: {msg.topic}")
    print(f"Payload: {msg.payload.decode()}")

def run_subscriber():
    client = mqtt.Client()

    client.on_connect = on_connect
    client.on_message = on_message

    print(f"Łączenie z brokerem MQTT {MQTT_HOST}:{MQTT_PORT}...")
    client.connect(MQTT_HOST, MQTT_PORT, keepalive=60)

    client.loop_forever()
