from backend.modules.temperature.parser import parse_payload
from backend.modules.temperature.insert import insert_temperature_data
from backend.db.sensor_repository import get_sensor_id_by_name
from backend.utils.logger import logger

def handle_temperature_message(topic: str, payload: str):
    logger.info(f"Odebrano dane z topica:{topic}")
    try:
        data = parse_payload(payload)
        if data is None:
            raise ValueError("Błąd parsowania payload")

        sensor_name = data["sensor_name"]
        sensor_id = get_sensor_id_by_name(sensor_name)
        if sensor_id is None:
            raise ValueError(f"Nie znaleziono sensora: {sensor_name}")

        insert_temperature_data(sensor_id, data["value"], data["timestamp"])
        logger.info("Dane zapisane do DB")
    except Exception as e:
        logger.error(f"Błąd przetwarzania wiadomości: {e}")
