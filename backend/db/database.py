import mysql.connector
from backend.config.config import DB_HOST,DB_NAME,DB_PASS,DB_USER

def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
    )

if __name__ == "__main__":
    try:
        conn = get_connection()
        print("✅ Połączenie z bazą danych działa!")
        conn.close()
    except Exception as e:
        print(f"❌ Błąd połączenia z bazą danych: {e}")