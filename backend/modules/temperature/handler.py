from modules.temperature.parser import parse_temperature_payload
from modules.temperature.insert import insert_temperature_data
from backend.utils.logger import logger

def handle_temperature_message(payload: str):
    try:
        data = parse_temperature_payload(payload)
        insert_temperature_data(data)
        logger.info("dane zapisane")
    except Exception as e:
        logger.error(f"błąd przetwarzania wiadomosci:{e}")
