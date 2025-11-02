from pymongo import MongoClient
from bson import ObjectId
import os


class enrollments_db_repo:
    def __init__(self):
        # self.__client = MongoClient(port=27017)
        # self.__client = MongoClient("mongodb+srv://rs0583221748_db_user:OwOmhGZKzyRojOpd@coursemanagerdb.mjca2e1.mongodb.net/?appName=CourseManagerDB")
        mongo_uri = os.getenv("MONGO_URI")  # קרא מה-Environment Variable
        self.__client = MongoClient(mongo_uri)
        self.__db = self.__client["project_4_subscriptions"]
        self.__collection = self.__db["enrollments"]

    def get_all_enrollments(self):
        enrollments = list(self.__collection.find({}))
        return enrollments

    def get_enrollment_by_id(self, id):
        enrollment = self.__collection.find_one({"_id": ObjectId(id)})
        return enrollment

    def add_enrollment(self, enrollment):
        result = self.__collection.insert_one(enrollment)
        return {"msg": f"Created with ID: {str(result.inserted_id)}"}

    def update_enrollment(self, id, enrollment):
        self.__collection.update_one({"_id": ObjectId(id)}, {"$set": enrollment})
        return {"msg": "Updated!"}

    def delete_enrollment(self, id):
        self.__collection.delete_one({"_id": ObjectId(id)})
        return {"msg": "Deleted!"}
