import json
from modules.common.handler import handle_sensor_data

def test_handle_sensor_data_success(monkeypatch):
    mock_data = {
        "sensor_name": "sensor_1",
        "value": 25.5,
        "timestamp": "2025-07-12 10:00:00"
    }

    payload = json.dumps({
        "sensor_name": mock_data["sensor_name"],
        "value": mock_data["value"]
    })

    def mock_parse(payload):
        return mock_data

    def mock_get_sensor_id(name):
        return 42

    def mock_insert(sensor_type, sensor_id, data):
        assert sensor_type == "temperature"
        assert sensor_id == 42
        assert data == mock_data

    monkeypatch.setattr("backend.modules.common.handler.parse_common_fields", mock_parse)
    monkeypatch.setattr("backend.modules.common.handler.get_sensor_id_by_name", mock_get_sensor_id)
    monkeypatch.setattr("backend.modules.common.handler.insert_sensor_data", mock_insert)

    handle_sensor_data("temperature", payload)


def test_handle_sensor_data_missing_sensor(monkeypatch):
    def mock_parse(payload):
        return {
            "sensor_name": "sensor_1",
            "value": 20.0,
            "timestamp": "2025-07-12 10:00:00"
        }

    def mock_get_sensor_id(name):
        return None

    def mock_insert(sensor_type, sensor_id, data):
        raise AssertionError("Nie powinno wywołać insert_sensor_data")

    monkeypatch.setattr("backend.modules.common.handler.parse_common_fields", mock_parse)
    monkeypatch.setattr("backend.modules.common.handler.get_sensor_id_by_name", mock_get_sensor_id)
    monkeypatch.setattr("backend.modules.common.handler.insert_sensor_data", mock_insert)

    payload = json.dumps({"sensor_name": "sensor_1", "value": 20.0})
    handle_sensor_data("temperature", payload)


def test_handle_sensor_data_parser_failure(monkeypatch):
    def mock_parse(payload):
        return None

    def mock_get_sensor_id(name):
        raise AssertionError("Nie powinno być wywołane")

    def mock_insert(sensor_type, sensor_id, data):
        raise AssertionError("Nie powinno być wywołane")

    monkeypatch.setattr("backend.modules.common.handler.parse_common_fields", mock_parse)
    monkeypatch.setattr("backend.modules.common.handler.get_sensor_id_by_name", mock_get_sensor_id)
    monkeypatch.setattr("backend.modules.common.handler.insert_sensor_data", mock_insert)

    payload = json.dumps({"sensor_name": "sensor_1", "value": 20.0})
    handle_sensor_data("temperature", payload)


def test_handle_sensor_data_insert_failure(monkeypatch):
    def mock_parse(payload):
        return {
            "sensor_name": "sensor_1",
            "value": 20.0,
            "timestamp": "2025-07-12 10:00:00"
        }

    def mock_get_sensor_id(name):
        return 42

    def mock_insert(sensor_type, sensor_id, data):
        raise Exception("Symulowany błąd inserta")

    monkeypatch.setattr("backend.modules.common.handler.parse_common_fields", mock_parse)
    monkeypatch.setattr("backend.modules.common.handler.get_sensor_id_by_name", mock_get_sensor_id)
    monkeypatch.setattr("backend.modules.common.handler.insert_sensor_data", mock_insert)

    payload = json.dumps({"sensor_name": "sensor_1", "value": 20.0})
    handle_sensor_data("temperature", payload)