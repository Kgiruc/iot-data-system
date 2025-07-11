from backend.modules.common.handler import handle_sensor_data
from backend.config.config import MQTT_TOPIC
from backend.utils.logger import logger

def dispatch(topic: str, payload: str):
    # Znajdź typ sensora pasujący do tego topicu
    sensor_type = next((stype for stype, t in MQTT_TOPIC.items() if t == topic), None)

    if sensor_type:
        handle_sensor_data(sensor_type, payload)
    else:
        logger.warning(f"Odrzucono wiadomość z nieznanego topica: {topic}")


