from backend.db.database import get_connection
from backend.utils.logger import logger

def insert_sensor_data(sensor_type: str, sensor_id: int, data: dict):
    table_name = f"{sensor_type.lower()}_data"
    value = data.get("value")
    timestamp = data.get("timestamp")

    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = f"""
        INSERT INTO {table_name} (sensor_id, value, timestamp)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (sensor_id, value, timestamp))
        conn.commit()

        logger.info(f"[{sensor_type}] Dane zapisane w tabeli {table_name}")
    except Exception as e:
        logger.error(f"[{sensor_type}] Błąd insertu: {e}")
        raise

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
