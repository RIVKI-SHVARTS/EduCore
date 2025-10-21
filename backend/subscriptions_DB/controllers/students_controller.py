from flask import Blueprint,jsonify,request
from services.student_service import student_service
from bson import ObjectId
from controllers.auth_middleware import token_required

students = Blueprint("students",__name__)
a_student = student_service()

def convert_objectid(doc):
    if isinstance(doc, list):
        return [convert_objectid(d) for d in doc]
    elif isinstance(doc, dict):
        return {k: convert_objectid(v) for k, v in doc.items()}
    elif isinstance(doc, ObjectId):
        return str(doc)
    else:
        return doc

@students.route("/", methods=["GET"], strict_slashes=False)
@token_required
def get_all():
    result = a_student.get_all_students()
    return jsonify(convert_objectid(result))

@students.route("/<string:id>", methods=["GET"],strict_slashes=False)
@token_required
def get_student(id):
    result = a_student.get_student_by_id(id)
    return jsonify(convert_objectid(result))

@students.route("/",methods = ["POST"])
@token_required
def add_student():
    obj = request.json
    result = a_student.add_student(obj)
    return jsonify(convert_objectid(result))

@students.route("/<string:id>" , methods = ["PUT"])
@token_required
def update_student(id):
    obj = request.json
    result = a_student.update_student(id,obj)
    return jsonify(convert_objectid(result))

@students.route("/<string:id>",methods = ["DELETE"])
@token_required
def delete_student(id):
    result = a_student.delete_student(id)
    return jsonify(convert_objectid(result))

