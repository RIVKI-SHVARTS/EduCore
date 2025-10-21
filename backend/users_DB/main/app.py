from flask import Flask, jsonify
from flask_cors import CORS
from flask.json.provider import DefaultJSONProvider
from bson import ObjectId
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__)
CORS(app, supports_credentials=True,
     origins="http://127.0.0.1:5500",
     allow_headers=["Content-Type", "Authorization"])

# מריץ CORS *קודם* ל־token_required
# CORS(app,
#      origins=["http://127.0.0.1:5500"],
#      supports_credentials=True,
#      allow_headers=["Content-Type", "Authorization"],
#      methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])

# JSON מותאם ל-ObjectId
class CustomJSONProvider(DefaultJSONProvider):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)

app.json = CustomJSONProvider(app)

# יבוא והגדרת ה-blueprints
from controllers.users_controllers import users
app.register_blueprint(users, url_prefix="/users")

from controllers.login_controller import login
app.register_blueprint(login, url_prefix="/login")

# מילוי משתמשים
from services.filling_in_service import StudentDataBuilder
users_inserter = StudentDataBuilder()
if users_inserter.is_db_empty():
    users_inserter.prepare_users_data()

@app.route("/", methods=["GET"])
def index():
    return "Server is running"

if __name__ == "__main__":
    app.run(port=8000, debug=True)
