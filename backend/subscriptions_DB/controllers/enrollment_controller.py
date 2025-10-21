from flask import Blueprint, jsonify, request
from services.enrollment_service import enrollment_service
from bson import ObjectId
from controllers.auth_middleware import token_required


enrollments = Blueprint("enrollments", __name__)
a_enrollment = enrollment_service()

def convert_objectid(doc):
    if isinstance(doc, list):
        return [convert_objectid(d) for d in doc]
    elif isinstance(doc, dict):
        return {k: convert_objectid(v) for k, v in doc.items()}
    elif isinstance(doc, ObjectId):
        return str(doc)
    else:
        return doc

@enrollments.route("/", methods=["GET"], strict_slashes=False)
@token_required
def get_all_enrollments():
    result = a_enrollment.get_all_enrollments()
    return jsonify(convert_objectid(result))

@enrollments.route("/<string:id>", methods=["GET"])
@token_required
def get_enrollment(id):
    result = a_enrollment.get_enrollment_by_id(id)
    return jsonify(convert_objectid(result))

@enrollments.route("/", methods=["POST"], strict_slashes=False)
@token_required
def add_enrollment():
    obj = request.json
    result = a_enrollment.add_enrollment(obj)
    return jsonify(convert_objectid(result))



@enrollments.route("/<string:id>", methods=["PUT"],strict_slashes=False)
@token_required
def update_enrollment(id):
    obj = request.json
    result = a_enrollment.update_enrollment(id, obj)
    return jsonify(convert_objectid(result))

@enrollments.route("/<string:id>", methods=["DELETE"])
@token_required
def delete_enrollment(id):
    result = a_enrollment.delete_enrollment(id)
    return jsonify(convert_objectid(result))


