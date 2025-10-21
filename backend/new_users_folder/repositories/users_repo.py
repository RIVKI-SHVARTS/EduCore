import json
import os


BASE_DIR = os.path.dirname(__file__)

class Users_repo:
    def __init__(self):
        self.path = os.path.abspath(os.path.join(BASE_DIR, "../data/users.json"))   

    def load_all_users(self):
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"File not found: {self.path}")
        with open(self.path, "r", encoding="utf-8") as fp:
            data = json.load(fp)
            return data

    def save_all_users(self,users):
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"File not found: {self.path}")
        with open(self.path, "w", encoding="utf-8") as fp:
            json.dump(users,fp,indent=4, ensure_ascii=False)
        