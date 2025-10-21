from repositories.student_repo import student_db_repo

class student_service:
    def __init__(self):
        self.student_repo = student_db_repo()

    def get_all_students(self):
        return self.student_repo.get_all_students()
    
    def get_student_by_id(self, id):
        return self.student_repo.get_student_by_id(id)
    
    def add_student(self, student):
        required_fields = ["name", "email", "city"]
        for field in required_fields:
            if field not in student or not student[field]:
                return f"Error: Missing required field '{field}'" 
          
        result = self.student_repo.add_student(student)
        return result["msg"]
    
    def update_student(self, id, student):
        required_fields = ["name", "email", "city"]
        for field in required_fields:
            if field not in student or not student[field]:
                return f"Error: Missing required field '{field}'"
        student.pop('_id', None)    
        result = self.student_repo.update_student(id, student)
        return result["msg"]
    
    def delete_student(self, id):
        result = self.student_repo.delete_student(id)
        return result["msg"]

    def is_db_empty(self):
        return self.student_repo.is_empty()