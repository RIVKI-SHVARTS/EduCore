from flask import Blueprint, jsonify, request
from repositories.permissions_repo import Permissions_repo

permissions_json = Blueprint("permissions_json", __name__)
repo = Permissions_repo()

# --- READ all permissions ---
@permissions_json.route("/", methods=["GET"])
def get_permissions_json():
    try:
        data = repo.load_all_permissions()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# --- CREATE (add a full permission record) ---
@permissions_json.route("/", methods=["POST"])
def create_permission_record():
    try:
        data = repo.load_all_permissions()
        new_permission_record = request.json
        data.append(new_permission_record)
        repo.save_all_permissions(data)
        return jsonify({"message": "Permission record created", 
                        "record": new_permission_record}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# --- UPDATE ---
@permissions_json.route("/<id>", methods=["PUT"])
def update_permission_record(id):
    try:
        data = repo.load_all_permissions()
        updated = request.json

        for i, record in enumerate(data):
            if record["id"] == id:
                data[i] = updated
                repo.save_all_permissions(data)
                return jsonify({"message": "Permission record updated", 
                                "record": updated})

        return jsonify({"error": "Permission record not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# --- DELETE ---
@permissions_json.route("/<id>", methods=["DELETE"])
def delete_permission_record(id):
    try:
        data = repo.load_all_permissions()
        new_list = [p for p in data if p["id"] != id]

        if len(new_list) == len(data):
            return jsonify({"error": "Permission record not found"}), 404

        repo.save_all_permissions(new_list)
        return jsonify({"message": "Permission record deleted"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
