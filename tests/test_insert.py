from backend.modules.common.insert import insert_sensor_data

def test_insert_sensor_data_invalid_table(monkeypatch):
    def mock_get_connection():
        class MockCursor:
            def execute(self, query, params):
                raise Exception("Symulowany błąd zapytania")
            def close(self): pass
        class MockConnection:
            def cursor(self): return MockCursor()
            def commit(self): pass
            def close(self): pass
        return MockConnection()

    monkeypatch.setattr("backend.modules.common.insert.get_connection", mock_get_connection)

    try:
        insert_sensor_data("unknown_sensor", 1, {
            "value": 22.5,
            "timestamp": "2025-07-12 12:00:00"
        })
        assert False, "Powinien być wyjątek"
    except Exception as e:
        assert "Symulowany błąd zapytania" in str(e)