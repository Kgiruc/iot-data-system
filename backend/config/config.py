from dotenv import load_dotenv
import os

base_dir = os.path.dirname(__file__)

load_dotenv(os.path.join(base_dir,"..",".env"))
load_dotenv(os.path.join(base_dir,"..","mqtt_topics.env"))

MQTT_HOST = os.getenv("MQTT_HOST")
MQTT_PORT = int(os.getenv("MQTT_PORT"))

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("MQTT_HOST")

MQTT_TOPIC = {
    key.removeprefix("MQTT_TOPIC_"): value
    for key, value in os.environ.items()
    if key.startswith("MQTT_TOPIC_")
}
print("mqtt_topic", MQTT_TOPIC)

