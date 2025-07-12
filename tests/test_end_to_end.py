import os
import time
import json
import paho.mqtt.client as mqtt
import mysql.connector
from dotenv import load_dotenv

# Załaduj zmienne środowiskowe z backend/.env
dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'backend', '.env')
load_dotenv(dotenv_path)

MQTT_HOST = os.getenv("MQTT_HOST")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

MQTT_TOPIC_TEST = os.getenv("MQTT_TEST_TOPIC")  # testowy topic, np. "test/test"

TABLE_TEMPERATURE = "temperature_data"


def on_connect(client, userdata, flags, rc):
    print(f"Połączono z MQTT, kod rc={rc}")


def on_disconnect(client, userdata, rc):
    print(f"Rozłączono z MQTT, kod rc={rc}")


def test_end_to_end():
    # Używamy protokołu MQTT 3.1.1 (bez callback_api_version)
    client = mqtt.Client(client_id="", protocol=mqtt.MQTTv311)

    client.on_connect = on_connect
    client.on_disconnect = on_disconnect

    client.connect(MQTT_HOST, MQTT_PORT, 60)

    payload = json.dumps({
        "sensor_name": "test_sensor",
        "value": 25.5
    })
    client.publish(MQTT_TOPIC_TEST, payload)
    client.disconnect()

    # Czekamy na backend, który odbierze i zapisze dane
    time.sleep(7)

    # Sprawdzenie czy dane trafiły do bazy
    conn = mysql.connector.connect(
        host=MQTT_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )
    cursor = conn.cursor()

    query = f"""
    SELECT value FROM {TABLE_TEMPERATURE}
    WHERE sensor_id = (SELECT id FROM sensors WHERE sensor_id = %s)
    ORDER BY timestamp DESC LIMIT 1
    """
    cursor.execute(query, ("test_sensor",))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    assert result is not None, "Dane nie zostały zapisane w bazie"
    assert abs(result[0] - 25.5) < 0.01, "Wartość w bazie nie zgadza się z wysłaną"