from pymongo import MongoClient
from bson import ObjectId
import os


class courses_db_repo:
    def __init__(self):
        # self.__client = MongoClient(port=27017)
        # self.__client = MongoClient("mongodb+srv://rs0583221748_db_user:OwOmhGZKzyRojOpd@coursemanagerdb.mjca2e1.mongodb.net/?appName=CourseManagerDB")
        mongo_uri = os.getenv("MONGO_URI")  # קרא מה-Environment Variable
        self.__client = MongoClient(mongo_uri)
        self.__db = self.__client["project_4_subscriptions"]
        self.__collection = self.__db["courses"]

    def get_all_courses(self):
        return list(self.__collection.find({}))

    def get_course_by_id(self, id):
        return self.__collection.find_one({"_id": ObjectId(id)})

    def add_course(self, course):
        self.__collection.insert_one(course)
        return {"msg": f"Created with ID: {course['_id']}"}

    def update_course(self, id, course):
        self.__collection.update_one({"_id": ObjectId(id)}, {"$set": course})
        return {"msg": "Updated!"}

    def delete_course(self, id):
        self.__collection.delete_one({"_id": ObjectId(id)})
        return {"msg": "Deleted!"}
    
    def is_empty(self):
        return self.__collection.count_documents({}) == 0

         





    

