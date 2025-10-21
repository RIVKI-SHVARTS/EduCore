import json
import os

BASE_DIR = os.path.dirname(__file__)
path = os.path.abspath(os.path.join(BASE_DIR, "../data/permissions.json"))

def load_all_permissions():
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    with open(path, "r", encoding="utf-8") as fp:
        data = json.load(fp)
        return data

def save_all_permissions(data):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    with open(path, "w", encoding="utf-8") as fp:
        json.dump(data,fp)

