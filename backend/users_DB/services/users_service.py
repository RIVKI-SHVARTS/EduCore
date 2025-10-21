from pymongo import MongoClient
from repositories.users_db_repo import db_repo
import bcrypt



class Users:
    def __init__(self):
        self.db_repo = db_repo()

    def get_all_users(self):
        return self.db_repo.get_all_users()
    
    def get_user_by_id(self,id):
        return self.db_repo.get_user_by_id(id)
    
    def get_user_by_username(self,username):
        return self.db_repo.get_user_by_username(username)
    
    def add_user(self,user):
        required_fields = ["firstName", "lastName","createdDate","sessionTimeOut","username","permissions"]
        for field in required_fields:
            if field not in user or not user[field]:
                return f"Error: Missing required field '{field}'" 
            
        # password_bytes = user["password"].encode("utf-8")
        # hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        # user["password"] = hashed_password
            
        result = self.db_repo.add_user(user)
        return result["msg"]

    def update_user(self, id, user):
        required_fields = ["id", "firstName", "lastName", "createdDate", "sessionTimeOut", "username", "permissions"]
        for field in required_fields:
            if field not in user or not user[field]:
                return f"Error: Missing required field '{field}'"

        # שליפת הסיסמה הקיימת אם לא נשלחה סיסמה חדשה
        if "password" not in user:
            existing_user = self.db_repo.get_user_by_id(id)
            if not existing_user:
                return "Error: User not found"
            user["password"] = existing_user["password"]
        else:
            password_bytes = user["password"].encode("utf-8")
            hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
            user["password"] = hashed_password

        result = self.db_repo.update_user(id, user)
        return result["msg"]


        

    def delete_user(self,id):
        result = self.db_repo.delete_user(id)
        return result["msg"]
