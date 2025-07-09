from backend.db.database import get_connection
from backend.utils.logger import logger

def insert_temperature_data(sensor_id, value, timestamp):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO temperature_data (sensor_id,value, timestamp)
        VALUES (%s,%s,%s)
        """
        cursor.execute(query,(sensor_id, value, timestamp))
        conn.commit()

        logger.info("dane zapisane")
    except Exception as e:
        logger.error(f"bład: {e}")
        return
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()