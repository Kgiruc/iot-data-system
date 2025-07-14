import pytest
import json
from services import mqtt_dispatcher
from config import config

def test_dispatch_valid_topic(monkeypatch):
    called = {}

    def mock_handle_sensor_data(sensor_type, payload):
        called["sensor_type"] = sensor_type
        called["payload"] = payload

    monkeypatch.setattr(mqtt_dispatcher, "handle_sensor_data", mock_handle_sensor_data)

    # Pobierz pierwszy topic i sensor_type z oryginalnej mapy (bez modyfikacji)
    sensor_type, topic = next(iter(config.MQTT_TOPIC.items()))

    payload = json.dumps({"sensor_name": "sensor_1", "value": 25.0})
    mqtt_dispatcher.dispatch(topic, payload)

    assert called["sensor_type"] == sensor_type
    assert called["payload"] == payload

def test_dispatch_unknown_topic_logs_warning(monkeypatch, caplog):
    def mock_handle_sensor_data(sensor_type, payload):
        pytest.fail("Nie powinno być wywołane")

    monkeypatch.setattr(mqtt_dispatcher, "handle_sensor_data", mock_handle_sensor_data)

    unknown_topic = "test/unknown_topic_1234"
    payload = json.dumps({"sensor_name": "sensor_1", "value": 25.0})

    with caplog.at_level("WARNING"):
        mqtt_dispatcher.dispatch(unknown_topic, payload)

    assert "Odrzucono wiadomość z nieznanego topica" in caplog.text