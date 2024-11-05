from flask import Flask, request, jsonify

app = Flask(__name__)

# Структура данных в памяти для пользователей, категорий и записей
users = {}
categories = {}
records = {}

# Пользователи
@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    user_id = len(users) + 1
    users[user_id] = {"id": user_id, "name": data["name"]}
    return jsonify(users[user_id]), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values()))

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"}), 200
    else:
        return jsonify({"error": "User not found"}), 404

# Категории
@app.route('/category', methods=['POST'])
def create_category():
    data = request.json
    category_id = len(categories) + 1
    categories[category_id] = {"id": category_id, "name": data["name"]}
    return jsonify(categories[category_id]), 201

@app.route('/category', methods=['GET'])
def get_categories():
    return jsonify(list(categories.values()))

@app.route('/category/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    if category_id in categories:
        del categories[category_id]
        return jsonify({"message": "Category deleted"}), 200
    else:
        return jsonify({"error": "Category not found"}), 404

# Записи о расходах
@app.route('/record', methods=['POST'])
def create_record():
    data = request.json
    record_id = len(records) + 1
    user_id = data["user_id"]
    category_id = data["category_id"]
    
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    if category_id not in categories:
        return jsonify({"error": "Category not found"}), 404
    
    records[record_id] = {
        "id": record_id,
        "user_id": user_id,
        "category_id": category_id,
        "timestamp": data.get("timestamp"),
        "amount": data["amount"]
    }
    return jsonify(records[record_id]), 201

@app.route('/record/<int:record_id>', methods=['GET'])
def get_record(record_id):
    record = records.get(record_id)
    if record:
        return jsonify(record)
    else:
        return jsonify({"error": "Record not found"}), 404

@app.route('/record/<int:record_id>', methods=['DELETE'])
def delete_record(record_id):
    if record_id in records:
        del records[record_id]
        return jsonify({"message": "Record deleted"}), 200
    else:
        return jsonify({"error": "Record not found"}), 404

@app.route('/record', methods=['GET'])
def get_records():
    user_id = request.args.get("user_id", type=int)
    category_id = request.args.get("category_id", type=int)
    
    if user_id is None and category_id is None:
        return jsonify({"error": "user_id or category_id parameter is required"}), 400

    filtered_records = [
        record for record in records.values()
        if (user_id is None or record["user_id"] == user_id) and
           (category_id is None or record["category_id"] == category_id)
    ]
    
    return jsonify(filtered_records)

if __name__ == '__main__':
    app.run(debug=True)
# Запись чисто для коммита, поскольку по какой-то причине не добавился коммит, когда я только начинал делать :(