import json
from modules.common.parser import parse_common_fields

def test_valid_payload(monkeypatch):
    def mock_validate_temperature(data):
        return True

    monkeypatch.setattr("backend.modules.common.parser.validate_temperature", mock_validate_temperature)

    payload = json.dumps({"sensor_name": "sensor_1", "value": 22.5})
    result = parse_common_fields(payload)

    assert result is not None
    assert result["sensor_name"] == "sensor_1"
    assert result["value"] == 22.5
    assert "timestamp" in result

def test_parser_invalid_json():
    payload = '"sensor_name": "sensor_1", "value": 22.5'  # Brak nawiasu
    result = parse_common_fields(payload)
    assert result is None

def test_parser_missing_fields():
    payload = json.dumps({"value": 22.5})  # Brak sensor_name
    result = parse_common_fields(payload)
    assert result is None

def test_parser_invalid_value(monkeypatch):
    def mock_validate_temperature(data):
        return False

    monkeypatch.setattr("backend.modules.common.parser.validate_temperature", mock_validate_temperature)

    payload = json.dumps({"sensor_name": "sensor_1", "value": "hot"})  # Zła wartość
    result = parse_common_fields(payload)
    assert result is None