import json
from backend.utils.logger import logger

def parse_payload(payload: str) -> dict | None:
    try:
        data = json.loads(payload)
        if not all(k in data for k in("sensor_id","value","unit","timestamp")):
            raise ValueError("brak wymaganych pól")
        return data
    except Exception as e:
        logger.error(f"bład parsownia:{e}")
        return None