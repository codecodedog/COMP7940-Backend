import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# Connection details
host = 'ls-d034ea5372313ffb138a7e4b821254e7da015cb0.canjvfiul751.ap-southeast-1.rds.amazonaws.com'
port = 3306
database = 'comp7940'
username = 'dbmasteruser'
password = 'xyAV$s`9k>93+C)iPwxt1G~NQzN=YEqs'

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