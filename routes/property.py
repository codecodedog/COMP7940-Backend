from flask import Blueprint, jsonify, request
from db import get_connection
from model.User import User
import json

property_bp = Blueprint('property', __name__)

@property_bp.route('/property', methods=['POST'])
def insert_property():
    data = request.get_json()

    user_id = data['user_id']
    district = data['district']
    address = data['address']
    condition = data['condition']
    is_rent = data['is_rent']
    price_min = data['price_min']
    price_max = data['price_max']
    paid_duration = data['paid_duration']

    connection = get_connection()
    if connection is None:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO property (user_id, district, address, `condition`, is_rent, price_min, price_max, paid_duration) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (user_id, district, address, condition, is_rent, price_min, price_max, paid_duration)
        )
        connection.commit()
        cursor.close()
        return jsonify({'result': data}), 200
    except Exception as e:
        connection.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        if connection is not None:
            connection.close()

@property_bp.route('/property/search', methods=['GET'])
def get_user_by_telegram():

    properties_preferences = []

    telegram_id = request.args.get('telegram_id')

    if not telegram_id:
        return jsonify({'error': 'telegram_id is required'}), 400

    connection = get_connection()
    if connection is None:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM user where telegram_id = " + str(telegram_id))
        user_result = cursor.fetchone()
        user = User(*user_result).to_dict()

        cursor.execute("SELECT * FROM property INNER JOIN user ON property.user_id = user.ID WHERE property.user_id <>" + str(user['ID']))
        propertyList = cursor.fetchall()

        for row in propertyList:
                
            properties_preferences.append({
                "district": row[2],
                "factor": json.loads(row[4]),
                "owner": {
                    "telegram_id": row[10],
                    "username": row[11],
                },
                "is_rent":  "Rent" if row[5] else "Leasing", 
                "address": row[3],
                "price_range": f"{row[6]} - {row[7]}",
                "paid_duration": row[8]
            })

        result = []

        for property in properties_preferences:
            if(any(item in property["factor"] for item in user['condition']) and property["district"] in user['preferred_district']):
                result.append(property)

        return jsonify(result), 200
        
    except Exception as e:
        connection.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        if connection is not None:
            connection.close()