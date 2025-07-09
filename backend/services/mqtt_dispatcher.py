from backend.modules.temperature.handler import handle_temperature_message
from backend.config.config import MQTT_TOPIC
from backend.utils.logger import logger

def dispatch(topic: str, payload: str):
    if topic == MQTT_TOPIC:
        handle_temperature_message(topic, payload)
    else:
        logger.warning(f"Otrzymano wiadomość z nieznanego tematu: {topic}")
