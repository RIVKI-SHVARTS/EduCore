from repositories.enrollment_repo import enrollments_db_repo

class enrollment_service:
    def __init__(self):
        self.enrollment_repo = enrollments_db_repo()

    def get_all_enrollments(self):
        return self.enrollment_repo.get_all_enrollments()
    
    def get_enrollment_by_id(self, id):
        return self.enrollment_repo.get_enrollment_by_id(id)

    def add_enrollment(self, enrollment):
        if "studentId" not in enrollment or not enrollment["studentId"]:
            return {"error": "Missing required field 'studentId'"}, 400

        if "courses" not in enrollment or enrollment["courses"] is None:
            enrollment["courses"] = []

        result = self.enrollment_repo.add_enrollment(enrollment)
        return {"msg": "Enrollment created", "enrollment": result}, 201


    def update_enrollment(self, id, enrollment):
        required_fields = ["studentId","courses"]
        for field in required_fields:
            if field not in enrollment or not enrollment[field]:
                return f"Error: Missing required field '{field}'"
        enrollment.pop('_id', None)
        result = self.enrollment_repo.update_enrollment(id, enrollment)
        return result["msg"]

    def delete_enrollment(self, id):
        result = self.enrollment_repo.delete_enrollment(id)
        return result["msg"]

