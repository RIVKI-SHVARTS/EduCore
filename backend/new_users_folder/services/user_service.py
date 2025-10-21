from pymongo import MongoClient
from repositories.users_db_repo import db_repo
from repositories.permissions_repo import Permissions_repo
from repositories.users_repo import Users_repo
import bcrypt



class Users_from_db:
    def __init__(self):
        self.db_repo = db_repo()
        self.users_repo = Users_repo()
        self.permissions_repo = Permissions_repo()

    def get_all_users(self):
        data_from_users_repo = self.users_repo.load_all_users()
        data_from_permissions_repo = self.permissions_repo.load_all_permissions()
        data_from_db = self.db_repo.get_all_usersname()
        
        users = []
        for user in data_from_db:
            user_obj = {**user}

            user_from_users_repo = next((u for u in data_from_users_repo if u["id"] == str(user["_id"])), None)
            if user_from_users_repo:
                user_obj["firstName"] = user_from_users_repo.get("firstName")
                user_obj["lastName"] = user_from_users_repo.get("lastName")
                user_obj["createdDate"] = user_from_users_repo.get("createdDate")
                user_obj["sessionTimeOut"] = user_from_users_repo.get("sessionTimeOut")

            user_from_permissions_repo = next((u for u in data_from_permissions_repo if u["id"] == str(user["_id"])), None)
            if user_from_permissions_repo:
                user_obj["permissions"] = user_from_permissions_repo.get("permissions", [])

            users.append(user_obj)

        return users


    def get_user_by_id(self, id):
        data_from_users_repo = self.users_repo.load_all_users()
        data_from_permissions_repo = self.permissions_repo.load_all_permissions()
        data_from_db = self.db_repo.get_username_by_id(id)

        if not data_from_db:
            return None 

        user_obj = {"_id":data_from_db["_id"],"username":data_from_db["username"]}
        print("DATA FROM DB:", data_from_db)
    

        user_from_users_repo = next((u for u in data_from_users_repo if u["id"] == str(data_from_db["_id"])), None)
        if user_from_users_repo:
            user_obj["firstName"] = user_from_users_repo.get("firstName")
            user_obj["lastName"] = user_from_users_repo.get("lastName")
            user_obj["createdDate"] = user_from_users_repo.get("createdDate")
            user_obj["sessionTimeOut"] = user_from_users_repo.get("sessionTimeOut")

        user_from_permissions_repo = next((u for u in data_from_permissions_repo if u["id"] == str(data_from_db["_id"])), None)
        if user_from_permissions_repo:
            user_obj["permissions"] = user_from_permissions_repo.get("permissions", [])

        return user_obj


    def get_user_by_username(self,username):
        data_from_users_repo = self.users_repo.load_all_users()
        data_from_permissions_repo = self.permissions_repo.load_all_permissions()
        data_from_db = self.db_repo.get_username_by_username(username)

        if not data_from_db:
            return None 

        user_obj = {"_id":data_from_db["_id"],"username":data_from_db["username"]}

        user_from_users_repo = next((u for u in data_from_users_repo if u["id"] == str(user_obj["_id"])), None)
        if user_from_users_repo:
            user_obj["firstName"] = user_from_users_repo.get("firstName")
            user_obj["lastName"] = user_from_users_repo.get("lastName")
            user_obj["createdDate"] = user_from_users_repo.get("createdDate")
            user_obj["sessionTimeOut"] = user_from_users_repo.get("sessionTimeOut")

        user_from_permissions_repo = next((u for u in data_from_permissions_repo if u["id"] == str(user_obj["_id"])), None)
        if user_from_permissions_repo:
            user_obj["permissions"] = user_from_permissions_repo.get("permissions", [])

        return user_obj

    
    def add_user(self, user):

        data_for_db = {"username": user["username"]}

        existing =  self.db_repo.get_username_by_username(user["username"])
        if existing:
            return {
                "status": "error",
                "message": "Username already exists"
            }

        self.db_repo.add_username(data_for_db)
        result =  self.db_repo.get_username_by_username(data_for_db["username"])
        user_id = result["_id"]


        data_for_user_json = {
            "id": str(user_id),
            "firstName": user["firstName"],
            "lastName": user["lastName"],
            "createdDate": user["createdDate"],
            "sessionTimeOut": user["sessionTimeOut"]
        }
        all_users_from_json = self.users_repo.load_all_users()
        print("all_users_from_json",all_users_from_json)
        all_users_from_json.append(data_for_user_json)
        self.users_repo.save_all_users(all_users_from_json)

        data_for_permissions_json = {
            "id": str(user_id),
            "permissions": user["permissions"]
        }
        all_permissions_from_json = self.permissions_repo.load_all_permissions()
        all_permissions_from_json.append(data_for_permissions_json)
        self.permissions_repo.save_all_permissions(all_permissions_from_json)

        return {
            "status": "success",
            "message": "User added successfully",
            "id": str(user_id)
        }




    def update_user(self, id, user):
        data_for_db = {"username": user["username"]}

        existing =  self.db_repo.get_username_by_id(id)
        if not existing:
            return {
                "status": "error",
                "message": "id is not exists"
            }

        self.db_repo.update_username(id, data_for_db)

        data_for_user_json = {
            "id": id,
            "firstName": user["firstName"],
            "lastName": user["lastName"],
            "createdDate": user["createdDate"],
            "sessionTimeOut": user["sessionTimeOut"]
        }

        all_users_from_json = self.users_repo.load_all_users()
        for i, u in enumerate(all_users_from_json):
            if u["id"] == id:
                all_users_from_json[i] = data_for_user_json
        self.users_repo.save_all_users(all_users_from_json)

        data_for_permissions_json = {
            "id": id,
            "permissions": user["permissions"]
        }
        all_permissions_from_json = self.permissions_repo.load_all_permissions()
        for i, p in enumerate(all_permissions_from_json):
            if p["id"] == id:
                all_permissions_from_json[i] = data_for_permissions_json
        self.permissions_repo.save_all_permissions(all_permissions_from_json)

        return {
            "status": "success",
            "message": "User updated successfully",
            "id": str(id)
        }
    


    
    def delete_user(self, id):
        existing =  self.db_repo.get_username_by_id(id)
        if not existing:
            return {
                "status": "error",
                "message": "id is not exists"
            }

        self.db_repo.delete_username(id)

        all_users_from_json = self.users_repo.load_all_users()
        all_users_from_json = [u for u in all_users_from_json if u["id"] != id]
        self.users_repo.save_all_users(all_users_from_json)

        all_permissions_from_json = self.permissions_repo.load_all_permissions()
        all_permissions_from_json = [p for p in all_permissions_from_json if p["id"] != id]
        self.permissions_repo.save_all_permissions(all_permissions_from_json)
  
        return {
            "status": "deleted",
            "message": "User deleted successfully",
            "id": str(id)
        }


