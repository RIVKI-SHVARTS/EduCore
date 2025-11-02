from pymongo import MongoClient
from bson import ObjectId

class student_db_repo:
    def __init__(self):
        # self.__client = MongoClient(port=27017)
        self.__client = MongoClient("mongodb+srv://rs0583221748_db_user:OwOmhGZKzyRojOpd@coursemanagerdb.mjca2e1.mongodb.net/?appName=CourseManagerDB")
        self.__db = self.__client["project_4_subscriptions"]
        self.__collection = self.__db["students"]

    def get_all_students(self):
        students = list(self.__collection.find({}))
        return students
    
    def get_student_by_id(self,id):
        student = self.__collection.find_one({"_id":ObjectId(id)})
        return student
    
    def add_student(self,student):
        result = self.__collection.insert_one(student)
        return {"msg": f"Created with ID: {result.inserted_id}"}
    
    def update_student(self,id,student):
        self.__collection.update_one({"_id":ObjectId(id)},{"$set":student})
        return {"msg":"Updated!"}
    
    def delete_student(self,id):
        self.__collection.delete_one({"_id": ObjectId(id)})
        return {"msg":"Deleted!"}

    def is_empty(self):
        return self.__collection.count_documents({}) == 0

    

