from backend.modules.common.parser import parse_common_fields
from backend.modules.common.insert import insert_sensor_data
from backend.validators.common.validate import load_validator
from backend.db.sensor_repository import get_sensor_id_by_name
from backend.utils.logger import logger

def handle_sensor_data(sensor_type: str, payload: str):
    logger.info(f"[{sensor_type}] Odebrano dane")
    try:
        validator = load_validator(sensor_type)
        validator.validate(payload)

        data = parse_common_fields(payload)
        sensor_name = data["sensor_name"]

        sensor_id = get_sensor_id_by_name(sensor_name)
        if sensor_id is None:
            raise ValueError(f"Nie znaleziono sensora: {sensor_name}")

        insert_sensor_data(sensor_type, sensor_id, data)
        logger.info(f"[{sensor_type}] Dane zapisane do DB")
    except Exception as e:
        logger.error(f"[{sensor_type}] Błąd przetwarzania wiadomości: {e}")
