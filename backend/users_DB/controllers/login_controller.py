from flask import Blueprint, jsonify, request
from services.login_service import login_service

login = Blueprint("login", __name__)
user_login = login_service()


@login.route("", methods=["POST", "OPTIONS"])
def connection_test():
    if request.method == "OPTIONS":
        # בקשת Preflight – מחזירים תשובה ריקה עם קוד הצלחה
        return '', 200

    data = request.json
    username = data.get("username")
    password = data.get("password")

    result = user_login.connection_test(username, password)

    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]

    return jsonify(result)

@login.route("/newUser", methods=["PUT"])
def add_password_to_new_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    result = user_login.add_password_to_new_user(username, password)

    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]

    return jsonify(result)

