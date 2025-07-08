from backend.modules.temperature.parser import parse_payload
from backend.modules.temperature.insert import insert_temperature_data
from backend.utils.logger import logger

def handle_temperature_message(topic, payload: str):
    try:
        data = parse_payload(payload)
        if not data:
            logger.error("Niepoprawny payload przerwanie handlera")
            return

        insert_temperature_data(
            sensor_id=data["sensor_id"],
            value=data["value"],
            unit=data["unit"],
            timestamp=data["timestamp"]
        )

        logger.info("Dane zapisane do DB")
    except Exception as e:
        logger.error(f"Błąd przetwarzania wiadomości: {e}")
