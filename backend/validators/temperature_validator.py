from backend.schemas.temperature_schame import TEMPERATURE_SCHEMA
from backend.validators.common.validate import validate_payload

def temperature_custom_rules(data:dict) -> bool:
    return data["unit"] == "C"

def validate_temperature(data: dict) -> bool:
    return validate_payload(data, TEMPERATURE_SCHEMA, temperature_custom_rules)