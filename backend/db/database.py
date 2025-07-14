import mysql.connector
from config.config import DB_HOST,DB_NAME,DB_PASS,DB_USER
from utils.logger import logger

def get_connection():
    try:
        conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
    )
        return conn
    except mysql.connector.Error as err:
        logger.error(f"Błąd połączenia z bazą danych: {err}")
        return None
