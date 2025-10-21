from flask import Blueprint,jsonify,request
from services.init_db_service import students_to_db,courses_to_db

add_students_to_db = Blueprint("add_students_to_db",__name__)
add_courses_to_db = Blueprint("add_courses_to_db",__name__)

students_insert = students_to_db()
courses_insert = courses_to_db()

@add_students_to_db.route("/",methods = ["POST"])
def add_students():
    obj = request.json
    result = students_insert.Insert_students_into_the_db(obj)
    return jsonify(result)

@add_courses_to_db.route("/",methods = ["POST"])
def add_courses():
    obj = request.json
    result = courses_insert.Insert_courses_into_the_db(obj)
    return jsonify(result)