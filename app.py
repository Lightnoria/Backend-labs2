import os

from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from passlib.hash import pbkdf2_sha256

# Настройки приложения
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "default_secret_key")  # Установите JWT ключ
jwt = JWTManager(app)

# Модели (заглушки)
users = {}  # Простой in-memory хранилище: username -> hashed_password

# ===== Аутентификация =====
@app.route('/auth/register', methods=['POST'])
def register():
    user_data = request.json
    username = user_data.get("username")
    password = user_data.get("password")

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400
    
    if username in users:
        return jsonify({"message": "User already exists"}), 400

    # Хэшируем пароль
    hashed_password = pbkdf2_sha256.hash(password)
    users[username] = hashed_password
    return jsonify({"message": f"User '{username}' registered successfully"}), 201


@app.route('/auth/login', methods=['POST'])
def login():
    user_data = request.json
    username = user_data.get("username")
    password = user_data.get("password")

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    # Проверяем пользователя
    if username in users and pbkdf2_sha256.verify(password, users[username]):
        access_token = create_access_token(identity=username)
        return jsonify({"access_token": access_token}), 200

    return jsonify({"message": "Invalid username or password"}), 401


# ===== Пример защищённого маршрута =====
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({"message": "Access granted!"}), 200


# Обработчики JWT ошибок
@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return jsonify({"message": "Missing authorization header"}), 401


@jwt.invalid_token_loader
def invalid_token_callback(callback):
    return jsonify({"message": "Invalid token"}), 401


# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True)
