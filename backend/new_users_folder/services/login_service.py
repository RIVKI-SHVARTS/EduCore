import bcrypt
from repositories.users_db_repo import db_repo
from repositories.users_repo import Users_repo
import jwt
from datetime import datetime, timedelta
from bson import ObjectId


SECRET_KEY = "very_secret" 

class login_service:
    def __init__(self):
        self.db_repo = db_repo()
        self.users_repo = Users_repo()

    def connection_test(self,username,password):
        user = self.db_repo.get_username_by_username(username)
        if not user:
            return {"error": "User not found"}, 404
        if bcrypt.checkpw(password.encode(), user["password"]):
            token = self.generate_token(user["_id"])
            return {"msg": "Login successful", "token": token}
        else:
            return {"error": "Invalid password"}, 401



    def add_password_to_new_user(self, username, password):
        try:
            user = self.db_repo.get_username_by_username(username)
            if not user:
                return {"error": "Unauthorized user"}, 404
            
            if user.get("password"):
                return{"error":"The user is already registered in the system. Try logging in again with your password."}
            
            user_id = ObjectId(user["_id"])
            hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            updated_user = {**user, "password": hashed_pw}
            response = self.db_repo.update_username(user_id, updated_user)
            if response.get("msg") == "Updated!":
                token = self.generate_token(user_id)
                return {"msg": "Login successful", "token": token}
            else:
                return {"error": "Update failed"}, 500

        except Exception as e:
            print("Error in add_password_to_new_user:", e)
            return {"error": "Internal server error"}, 500


 
    
         

     

    def generate_token(self,user_id):
        allUsers = self.users_repo.load_all_users()
        user = next((u for u in allUsers if str(u["id"]) == str(user_id)), None)
        payload = {
            "user_id": str(user_id),
            "exp": datetime.utcnow() + timedelta(minutes = user["sessionTimeOut"])
    

        }
        return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    def verify_token(self,token):
        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return decoded
        except jwt.ExpiredSignatureError:
            return {"error": "Token expired"}, 401
        except jwt.InvalidTokenError:
            return {"error": "Invalid token"}, 401
        

        


        
