from flask import Flask, request, jsonify

app = Flask(__name__)

# Глобальные переменные для хранения данных
users = {}
categories = {}
records = {}

@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    user_id = len(users) + 1
    users[user_id] = {"id": user_id, "name": data["name"]}
    return jsonify(users[user_id]), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values()))

if __name__ == '__main__':
    app.run(debug=True)
