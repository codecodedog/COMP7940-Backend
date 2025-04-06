import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# Connection details
host = os.getenv('DB_ENDPOINT')
port = 3306
database = os.getenv('DB_NAME')
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')

def get_connection():
    # Establish connection
    conn = mysql.connector.connect(
        host=host,
        port=port,
        database=database,
        user=username,
        password=password
    )

    cursor = conn.cursor()
    print("Connection established successfully!")
    return conn
    
if __name__ == "__main__":
    get_connection()