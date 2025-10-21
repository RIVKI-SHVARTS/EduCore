from functools import wraps
# from flask import request, jsonify
from flask import request, jsonify, make_response
import jwt

SECRET_KEY = "very_secret"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # אם זו בקשת preflight – נחזיר 204 ונעבור הלאה
        if request.method == "OPTIONS":
            return make_response(("", 204))
        
        # … כאן שאר בדיקת הטוקן שלך …
        token = request.headers.get("Authorization", None)
        if not token:
            return jsonify({"message": "Token is missing"}), 401
        # בדיקה ו־decode של הטוקן…
        
        return f(*args, **kwargs)
    return decorated


# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = None

#         if "Authorization" in request.headers:
#             auth_header = request.headers["Authorization"]
#             if auth_header.startswith("Bearer "):
#                 token = auth_header.split(" ")[1]

#         if not token:
#             return jsonify({"error": "Token is missing!"}), 401

#         try:
#             decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
#         except jwt.ExpiredSignatureError:
#             return jsonify({"error": "Token has expired!"}), 401
#         except jwt.InvalidTokenError:
#             return jsonify({"error": "Invalid token!"}), 401

#         return f(*args, **kwargs)

#     return decorated

