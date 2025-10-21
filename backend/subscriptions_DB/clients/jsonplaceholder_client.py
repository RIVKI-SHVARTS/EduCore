import requests

class students:
    def __init__(self):
        self.url = "https://jsonplaceholder.typicode.com/users"

    def get_all_students(self):
        resp = requests.get(self.url)
        students = resp.json()
        return students

    def get_student_by_id(self, id):
        resp = requests.get(f"{self.url}/{id}")
        student = resp.json()
        return student

    def add_student(self, student):
        resp = requests.post(self.url, json=student)
        new_student = resp.json()
        return "msg: student added successfully"

    def update_student(self, id, data):
        resp = requests.put(f"{self.url}/{id}", json=data)
        updated_student = resp.json()
        return "msg: student updated successfully"

    def delete_students(self, id):
        resp = requests.delete(f"{self.url}/{id}")
        return "msg: student deleted successfully"
