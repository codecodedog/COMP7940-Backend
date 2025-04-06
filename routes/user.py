from flask import Blueprint, jsonify, request
from db import get_connection
from model.User import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/user/telegram', methods=['GET'])
def get_user_by_telegram():

    telegram_id = request.args.get('telegram_id')

    if not telegram_id:
        return jsonify({'error': 'telegram_id is required'}), 400

    connection = get_connection()
    if connection is None:
        return jsonify({'error': 'Database connection failed'}), 500

    cursor = connection.cursor()
    query = "SELECT * FROM user WHERE telegram_id = %s AND isActive = 1"
    cursor.execute(query, (telegram_id,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()

    user = User(*result).to_dict()

    if result:
        return jsonify(user), 200
    else:
        return jsonify({'result': 'User not found or inactive'}), 404
    
@user_bp.route('/user', methods=['POST'])
def insert_user():
    data = request.get_json()

    telegram_id = data['telegram_id']
    username = data['username']
    condition = data['condition']
    preferred_district = data['preferred_district']
    isActive = data['isActive']

    connection = get_connection()
    if connection is None:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO user (telegram_id, username, `condition`, preferred_district, isActive) "
            "VALUES (%s, %s, %s, %s, %s)",
            (telegram_id, username, condition, preferred_district, isActive)
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

@user_bp.route('/user', methods=['PUT'])
def update_user():
    data = request.get_json()

    telegram_id = data['telegram_id']
    username = data['username']
    condition = data['condition']
    preferred_district = data['preferred_district']
    isActive = data['isActive']

    connection = get_connection()
    if connection is None:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE user SET username = %s, `condition` = %s, preferred_district = %s, isActive = %s "
            "WHERE telegram_id = %s",
            (username, condition, preferred_district, 1, telegram_id)
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