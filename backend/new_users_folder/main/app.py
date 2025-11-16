from flask import Flask, jsonify
from flask_cors import CORS
from flask.json.provider import DefaultJSONProvider
from bson import ObjectId
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__)
# CORS(app, supports_credentials=True,
#      origins="http://127.0.0.1:5500",
#      allow_headers=["Content-Type", "Authorization"])

# CORS(app,
#      supports_credentials=True,
#      origins=["*"],
#      allow_headers=["Content-Type", "Authorization"],
#      methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])

CORS(app,
     supports_credentials=True,
     origins=["https://educore-frontend-x84p.onrender.com"],
     allow_headers=["Content-Type", "Authorization"],
     methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])


class CustomJSONProvider(DefaultJSONProvider):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)

app.json = CustomJSONProvider(app)

from controllers.users_controllers import users
app.register_blueprint(users, url_prefix="/users")

from controllers.login_controller import login
app.register_blueprint(login, url_prefix="/login")

@app.route("/", methods=["GET"])
def index():
    return "Server is running"

if __name__ == "__main__":
    app.run(port=8000, debug=True)
