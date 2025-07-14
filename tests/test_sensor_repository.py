from db.sensor_repository import get_sensor_id_by_name

def test_get_sensor_id_success(monkeypatch):
    def mock_get_connection():
        class MockCursor:
            def execute(self, query, params): pass
            def fetchone(self): return (42,)
            def close(self): pass
        class MockConn:
            def cursor(self): return MockCursor()
            def close(self): pass
        return MockConn()

    monkeypatch.setattr("db.sensor_repository.get_connection", mock_get_connection)
    result = get_sensor_id_by_name("sensor_1")
    assert result == 42


def test_get_sensor_id_not_found(monkeypatch):
    def mock_get_connection():
        class MockCursor:
            def execute(self, query, params): pass
            def fetchone(self): return None
            def close(self): pass
        class MockConn:
            def cursor(self): return MockCursor()
            def close(self): pass
        return MockConn()

    monkeypatch.setattr("db.sensor_repository.get_connection", mock_get_connection)
    result = get_sensor_id_by_name("sensor_x")
    assert result is None


def test_get_sensor_id_db_error(monkeypatch):
    def mock_get_connection():
        raise Exception("DB error")

    monkeypatch.setattr("db.sensor_repository.get_connection", mock_get_connection)
    result = get_sensor_id_by_name("sensor_err")
    assert result is None