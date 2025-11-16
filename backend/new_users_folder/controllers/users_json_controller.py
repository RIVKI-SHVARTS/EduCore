from flask import Blueprint, jsonify, request
from repositories.users_repo import Users_repo

users_json = Blueprint("users_json", __name__)
repo = Users_repo()

# --- READ ---
@users_json.route("/", methods=["GET"])
def get_users_json():
    try:
        data = repo.load_all_users()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# --- CREATE ---
@users_json.route("/", methods=["POST"])
def create_user_json():
    try:
        data = repo.load_all_users()
        new_user = request.json
        data.append(new_user)
        repo.save_all_users(data)
        return jsonify({"message": "User created", "user": new_user}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# --- UPDATE ---
@users_json.route("/<id>", methods=["PUT"])
def update_user_json(id):
    try:
        data = repo.load_all_users()
        updated = request.json

        for i, user in enumerate(data):
            if user["id"] == id:
                data[i] = updated
                repo.save_all_users(data)
                return jsonify({"message": "User updated", "user": updated})

        return jsonify({"error": "User not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# --- DELETE ---
@users_json.route("/<id>", methods=["DELETE"])
def delete_user_json(id):
    try:
        data = repo.load_all_users()
        new_list = [u for u in data if u["id"] != id]

        if len(new_list) == len(data):
            return jsonify({"error": "User not found"}), 404

        repo.save_all_users(new_list)
        return jsonify({"message": "User deleted"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
