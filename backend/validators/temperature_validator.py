from backend.schemas.temperature_schema import TEMPERATURE_SCHEMA
from backend.validators.common.validate import validate_payload

def validate_temperature(data: dict) -> bool:
    return validate_payload(data, TEMPERATURE_SCHEMA)