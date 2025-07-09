import json
from datetime import datetime, timezone
from backend.utils.logger import logger


def parse_payload(payload: str) -> dict | None:
    try:
        data = json.loads(payload)
        if not all(k in data for k in("sensor_name","value")):
            raise ValueError("brak wymaganych pól")
        
        data["timestamp"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        return data
    except Exception as e:
        logger.error(f"bład parsownia:{e}")
        return None