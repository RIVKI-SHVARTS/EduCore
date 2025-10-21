from flask import Blueprint, jsonify, request
from services.course_service import course_service
from bson import ObjectId
from controllers.auth_middleware import token_required


courses = Blueprint("courses", __name__ )
a_course = course_service()

def convert_objectid(doc):
    if isinstance(doc, list):
        return [convert_objectid(d) for d in doc]
    elif isinstance(doc, dict):
        return {k: convert_objectid(v) for k, v in doc.items()}
    elif isinstance(doc, ObjectId):
        return str(doc)
    else:
        return doc
    
@courses.route("/", methods=["GET"] , strict_slashes=False)
@token_required
def get_all_courses():
    result = a_course.get_all_courses()
    return jsonify(convert_objectid(result))

@courses.route("/<string:id>", methods=["GET"])
@token_required
def get_course(id):
    result = a_course.get_course_by_id(id)
    return jsonify(convert_objectid(result))

@courses.route("/", methods=["POST"],strict_slashes=False)
@token_required
def add_course():
    obj = request.json
    print("Received data:", obj)

    result = a_course.add_course(obj)
    return jsonify(convert_objectid(result))

@courses.route("/<string:id>", methods=["PUT"],strict_slashes=False)
@token_required
def update_course(id):
    obj = request.json
    result = a_course.update_course(id, obj)
    return jsonify(convert_objectid(result))

@courses.route("/<string:id>", methods=["DELETE"])
@token_required
def delete_course(id):
    result = a_course.delete_course(id)
    return jsonify(convert_objectid(result))
