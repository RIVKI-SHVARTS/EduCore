import json
import os
import sys

class courses:
    def __init__(self):
        self.__path = os.path.join(sys.path[0], "../data/courses.json")

    def get_all_courses(self):
        with open(self.__path,"r")as fp:
            data = json.load(fp)
            return data
        
    def get_course_by_id(self,id):
        all_courses = self.get_all_courses()
        for course in all_courses:
            if course["id"] == id:
                return course
        return None
    
    def get_course_by_name(self,name):
        all_courses = self.get_all_courses()
        for course in all_courses:
            if course["name"] == name:
                return course
        return None
    
    def save_all_courses(self, courses):
        with open(self.__path, "w") as fp:
            json.dump(courses, fp, indent=2)

        
    def add_course(self, new_course):
        courses = self.get_all_courses()
        courses.append(new_course)         
        self.save_all_courses(courses) 

    def update_course(self, id, data):
        courses = self.get_all_courses()
        for course in courses:
            if course["id"] == id:
                course.update(data)
                self.save_all_courses(courses)
                return course
        return None
    

    def delete_course(self,id):
        courses = self.get_all_courses()
        for course in courses:
            if course["id"] == id:
                courses.remove(course)
                self.save_all_courses(courses)
                return course
        return None
    
    


        
# c = courses()
# data = c.get_course_by_id(3)  
# print(data)
            