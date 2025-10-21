from pymongo import MongoClient
from bson import ObjectId

class db_repo:
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["project_4_users_DB"]
        self.__collection = self.__db["users"]


    def get_all_usersname(self):
        return list(self.__collection.find({}))


    def get_username_by_id(self,id):
        user_data = self.__collection.find_one({"_id": ObjectId(id)})
        return user_data
    
    def get_password_by_id(self,id):
        user_data = self.__collection.find_one({"_id": ObjectId(id)})
        return user_data["password"]
    
    def get_username_by_username(self,username):
        return self.__collection.find_one({"username":username})
    

    def add_username(self,user):
        user.pop("_id", None)  
        result = self.__collection.insert_one(user)
        return {"msg": f"Created with ID: {result.inserted_id}"}
    
    def update_username(self,id,user):
        user.pop("_id", None)  
        result =self.__collection.update_one({"_id":ObjectId(id)},{"$set":user})
        return {"msg": "Updated!"}
    
    
    def delete_username(self,id):
        result = self.__collection.delete_one({"_id": ObjectId(id)})
        return {"msg": "Deleted!"}


        
         