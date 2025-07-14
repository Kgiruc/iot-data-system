from validators.temperature_validator import validate_temperature

def test_valid_temperature():
    data = {"sensor_name": "temp1", "value": 22.5}
    assert validate_temperature(data) is True

def test_missing_value():
    data = {"sensor_name": "temp1"}
    assert validate_temperature(data) is False

def test_invalid_type():
    data = {"sensor_name": "temp1", "value": "hot"}
    assert validate_temperature(data) is False