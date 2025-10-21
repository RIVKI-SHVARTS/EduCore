from pymongo import MongoClient
from bson import ObjectId

class db_repo:
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["project_4_users_DB"]
        self.__collection = self.__db["users"]


    def get_all_users(self):
        return list(self.__collection.find({}))


    def get_user_by_id(self,id):
        return self.__collection.find_one({"_id": ObjectId(id)})
    
    def get_user_by_username(self,username):
        return self.__collection.find_one({"username":username})
    

    def add_user(self,user):
        user.pop("_id", None)  
        result = self.__collection.insert_one(user)
        return {"msg": f"Created with ID: {result.inserted_id}"}


    def add_users(self,users):
        result = self.__collection.insert_many(users)
        return {"msg": "Students added successfully"}
    

    def update_user(self,id,user):
        user.pop("_id", None)  
        result =self.__collection.update_one({"_id":ObjectId(id)},{"$set":user})
        return {"msg": "Updated!"}
    
    

    def delete_user(self,id):
        result = self.__collection.delete_one({"_id": ObjectId(id)})
        return {"msg": "Deleted!"}


    def is_empty(self):
        return self.__collection.count_documents({}) == 0
        
         