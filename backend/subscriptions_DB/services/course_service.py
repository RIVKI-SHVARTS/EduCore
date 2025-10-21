from repositories.course_repo import courses_db_repo

class course_service:
    def __init__(self):
        self.course_repo = courses_db_repo()

    def get_all_courses(self):
        return self.course_repo.get_all_courses()

    def get_course_by_id(self, _id):
        return self.course_repo.get_course_by_id(_id)

    def add_course(self, course):
        required_fields = ["category","image","name","startDate"]
        for field in required_fields:
            if field not in course or not course[field]:
                return f"Error: Missing required field '{field}'"
        
        result = self.course_repo.add_course(course)
        return result["msg"]

    def update_course(self, _id, course):
        required_fields = ["category","image","name","startDate"]
        for field in required_fields:
            if field not in course or not course[field]:
                return f"Error: Missing required field '{field}'"
        course.pop('_id', None)
        result = self.course_repo.update_course(_id, course)
        return result["msg"]

    def delete_course(self, _id):
        result = self.course_repo.delete_course(_id)
        return result["msg"]

    def is_db_empty(self):
        return self.course_repo.is_empty()