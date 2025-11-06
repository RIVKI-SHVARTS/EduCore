import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
from flask import Flask,jsonify
from bson import ObjectId
from flask_cors import CORS

from services.init_db_service import courses_to_db, students_to_db

# app = Flask(__name__)

# CORS(app)
# app = Flask(__name__)
# CORS(app, supports_credentials=True,
#      origins="http://127.0.0.1:5500",
#      allow_headers=["Content-Type", "Authorization"])

app = Flask(__name__)
CORS(app,
     supports_credentials=True,
     origins=["*"],
     allow_headers=["Content-Type", "Authorization"],
     methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

app.json_encoder = JSONEncoder

from controllers.students_controller import students
app.register_blueprint(students, url_prefix="/students")

from controllers.courses_controller import courses
app.register_blueprint(courses, url_prefix="/courses")

from controllers.enrollment_controller import enrollments
app.register_blueprint(enrollments, url_prefix="/enrollments")

students_inserter = students_to_db()
courses_inserter = courses_to_db()

if students_inserter.is_db_empty():
    students_inserter.Insert_students_into_the_db()

if courses_inserter.is_db_empty():
    courses_inserter.Insert_courses_into_the_db()

app.run(port=8800,  debug=True)
# app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8800)), debug=True)

