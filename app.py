import os
from flask import Flask
from routes.user import user_bp
from routes.property import property_bp

app = Flask(__name__)

app.register_blueprint(user_bp)
app.register_blueprint(property_bp)

host = os.getenv('DB_ENDPOINT')
port = 3306
database = os.getenv('DB_NAME')
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')

print(host, port, database, username, password)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)