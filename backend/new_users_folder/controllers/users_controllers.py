from flask import Blueprint, jsonify, request
from services.user_service import Users_from_db
from bson import ObjectId
from controllers.auth_middleware import token_required



users = Blueprint("users", __name__)
a_student = Users_from_db ()

def convert_objectid(doc):
    if isinstance(doc, list):
        return [convert_objectid(d) for d in doc]
    elif isinstance(doc, dict):
        return {k: convert_objectid(v) for k, v in doc.items()}
    elif isinstance(doc, ObjectId):
        return str(doc)
    else:
        return doc

def remove_password(users):
    for user in users:
        user.pop("password", None)
    return users
    
def remove_password_from_user(user):
    user.pop("password", None)
    return user

@users.route("",methods = ["GET"])
@token_required
def get_all_users():
    result = a_student.get_all_users()
    return jsonify(remove_password(result))


@users.route("/<string:id>",methods = ["GET"])
@token_required
def get_user(id):
    result = a_student.get_user_by_id(id)
    return jsonify(remove_password_from_user(result))

@users.route("/username/<string:username>", methods=["GET"])
@token_required
def get_user_by_username(username):
    result = a_student.get_user_by_username(username)
    result = convert_objectid(result)
    return jsonify(remove_password_from_user(result))


@users.route("/",methods =["POST"])
@token_required
def add_user():
    obj = request.json
    result = a_student.add_user(obj)
    return jsonify(convert_objectid(result)) 


@users.route("/<string:id>", methods = ["PUT"])
@token_required
def update_user(id):
    obj = request.json
    result = a_student.update_user(id, obj)
    return jsonify(convert_objectid(result))


@users.route("/<string:id>",methods =["DELETE"])
@token_required
def delete_user(id):
    result = a_student.delete_user(id)
    return jsonify(convert_objectid(result))
    

