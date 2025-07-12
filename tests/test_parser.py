from backend.modules.common.parser import parse_common_fields
import json

def test_valid_payload(monkeypatch):
    def mock_validate_temperature(data):
        return True

    monkeypatch.setattr("backend.modules.common.parser.validate_temperature", mock_validate_temperature)

    payload = json.dumps({"sensor_name": "sensor_1", "value": 22.5})
    result = parse_common_fields(payload)

    assert result is not None
    assert result["sensor_name"] == "sensor_1"
    assert "timestamp" in result
