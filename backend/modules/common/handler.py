from modules.common.parser import parse_common_fields
from modules.common.insert import insert_sensor_data
from db.sensor_repository import get_sensor_id_by_name
from utils.logger import logger

def handle_sensor_data(sensor_type: str, payload: str):
    logger.info(f"[{sensor_type.upper()}] Odebrano payload: {payload}")

    try:
        data = parse_common_fields(payload)
        if not data:
            raise ValueError("Błąd parsowania danych")

        sensor_name = data["sensor_name"]
        sensor_id = get_sensor_id_by_name(sensor_name)
        if not sensor_id:
            raise ValueError(f"Nie znaleziono sensora: {sensor_name}")

        insert_sensor_data(sensor_type, sensor_id, data)
        logger.info("Dane zapisane do DB")
    
    except Exception as e:
        logger.error(f"[{sensor_type.upper()}] Błąd przetwarzania: {e}")
