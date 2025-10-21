from clients.jsonplaceholder_client import students
from repositories.student_repo import student_db_repo
from clients.json_courses_client import courses
from repositories.course_repo import courses_db_repo

class students_to_db:
    def __init__(self):
        self.students = students()
        self.db_repo = student_db_repo()

    def Insert_students_into_the_db(self):
        data = self.students.get_all_students()
        for s in data:  
            student_data = {  
                "name": s["name"],
                "email": s["email"],
                "city": s["address"]["city"]
            }
            self.db_repo.add_student(student_data)

    def is_db_empty(self):
        return self.db_repo.is_empty()


        

class courses_to_db:
    def __init__(self):
        self.courses = courses()
        self.db_repo = courses_db_repo()

    def Insert_courses_into_the_db(self):
        courses = self.courses.get_all_courses()
        for c in courses:
            self.db_repo.add_course(c)
        print("courses loaded from JSON file.")

    def is_db_empty(self):
        return self.db_repo.is_empty()



        

        

