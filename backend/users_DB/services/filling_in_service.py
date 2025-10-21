import bcrypt

from repositories.users_repo import get_user
from backend.users_DB.data.Login_repo import get_username_and_password
from repositories.permissions_repo import get_permissions
from repositories.users_db_repo import db_repo

class StudentDataBuilder:
    def __init__(self):
        self.users = get_user() 
        self.user_credentials = get_username_and_password() 
        self.user_permissions = get_permissions() 
        self.db_repo = db_repo()

    def prepare_users_data(self):
        all_users_data = []

        for u in self.users:
            user_data = {
                # "id": u["id"],
                "firstName": u["firstName"],
                "lastName": u["lastName"],
                "createdDate": u["createdDate"],
                "sessionTimeOut": u["sessionTimeOut"]
            }

       
            credentials_matches = list(filter(lambda cred: cred["id"] == u["id"], self.user_credentials))

     
            permissions_matches = list(filter(lambda p: p["id"] == u["id"], self.user_permissions))

            # אם נמצאה התאמה ב-credentials, נשלוף את שם המשתמש ונצפין את הסיסמה
            if credentials_matches:
                username = credentials_matches[0]["username"]
                raw_password = credentials_matches[0]["password"]
                # הצפנת הסיסמה ב־bcrypt
                hashed_pw = bcrypt.hashpw(raw_password.encode(), bcrypt.gensalt())
            else:
                username = None
                hashed_pw = None

            # עדכון האובייקט עם שדות נוספים
            user_data.update({
                "username": username,
                "password": hashed_pw,  # שמירת הסיסמה המוצפנת
                "permissions": permissions_matches[0]["permissions"] if permissions_matches else None
            })

            all_users_data.append(user_data)

        self.db_repo.add_users(all_users_data)

    def is_db_empty(self):
        return self.db_repo.is_empty()
