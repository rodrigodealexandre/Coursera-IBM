import psycopg2
import traceback

try:
    connection = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="postgres",
        host="192.168.0.12",
        port="5432"
    )
    print("Connection successful")
except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()
