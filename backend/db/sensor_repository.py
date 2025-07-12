from backend.db.database import get_connection
from backend.utils.logger import logger

def get_sensor_id_by_name(sensor_id: str) -> int | None:
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT id FROM sensors WHERE sensor_id = %s"
        cursor.execute(query, (sensor_id,))
        result = cursor.fetchone()
        return result[0] if result else None
    except Exception as e:
        logger.error(f"Błąd przy pobieraniu sensor_id: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()