from backend.modules.temperature.handler import handle_temperature_message
from backend.utils.logger import logger

def dispatch(topic: str, payload: str):
    if topic == "sensors/temperature":
        handle_temperature_message(payload.encode())
    else:
        logger.warning(f"Otrzymano wiadomość z nieznanego tematu: {topic}")
