import json
import os

BASE_DIR = os.path.dirname(__file__)
path = os.path.abspath(os.path.join(BASE_DIR, "../data/Login_users.json"))

def get_username_and_password():
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    with open(path, "r", encoding="utf-8") as fp:
        data = json.load(fp)
        return data
