from flask import Flask
from routes.user import user_bp
from routes.property import property_bp

app = Flask(__name__)

app.register_blueprint(user_bp)
app.register_blueprint(property_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)