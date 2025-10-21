from functools import wraps
# from flask import request, jsonify
from flask import request, jsonify, make_response
import jwt

SECRET_KEY = "very_secret"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if request.method == "OPTIONS":
            return make_response(("", 204))
        
        token = request.headers.get("Authorization", None)
        if not token:
            return jsonify({"message": "Token is missing"}), 401
        
        return f(*args, **kwargs)
    return decorated


