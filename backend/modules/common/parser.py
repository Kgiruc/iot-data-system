import json
from datetime import datetime, timezone
from backend.utils.logger import logger
from backend.validators.temperature_validator import validate_temperature

def parse_common_fields(payload: str) -> dict | None:
    try:
        data = json.loads(payload)
        if not all(k in data for k in ("sensor_name", "value")):
            raise ValueError("Brak wymaganych pól")
        
        if not validate_temperature(data):
            raise ValueError("Walidacja nie powiodła się")


        data["timestamp"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        return data

    except Exception as e:
        logger.error(f"Błąd parsowania: {e}")
        return None