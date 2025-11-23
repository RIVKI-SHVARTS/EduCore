EduCore – Course, Users & Enrollment Management System

EduCore is a full-stack management platform built with two independent Flask REST API servers and a deployed HTML/CSS/JavaScript frontend.

The system manages users, courses, students and enrollments, with secure authentication, authorization and full CRUD functionality. The project is fully deployed online and runs entirely in the cloud.

Live System URLs:
Frontend (Client): 
https://educore-frontend-x84p.onrender.com/

Users Server (Authentication & User Management): 
https://educore-m9yh.onrender.com/

Courses, Students & Enrollments Server: 
https://educore-subscriptions-db.onrender.com/

Demo Login (Read-Only Access):
username: demo
password: Demo1234

This demo account allows recruiters to explore the system without creating a new user.  
The demo user has limited permissions and cannot modify or delete real data.


System Overview:
The EduCore system consists of:
1. Users Server (new_users_folder)
   - Manages users, login, registration, bcrypt hashing, JWT tokens, permissions.
   - Stores user data in MongoDB.
   - Provides authentication middleware to secure all protected routes.

2. Courses/Enrollments Server (subscriptions_DB)
   - Manages courses, students, and enrollments.
   - Loads initial data from JSON clients.
   - Exposes REST API for all CRUD operations.
   - Also uses MongoDB as storage.

3. Frontend (HTML/CSS/JS)
   - Located originally in docs/frontend.
   - Fully deployed to the web.
   - Communicates directly with both backend servers using fetch() and authorization headers.
   - Provides pages for viewing, editing and managing all data.

Main Features:
- Two Flask servers working together in a multi-service architecture.
- Secure authentication using bcrypt password hashing.
- Authorization using JWT tokens saved in sessionStorage.
- Fully cloud-deployed backend and frontend.
- Complete management: Users, Courses, Students, Enrollments.
- Clear folder structure with controllers, services, repositories and data layers.
- RESTful communication between client and both servers.
- JSON-based initial data import for courses and students.
- Responsive and interactive frontend.

Cloud Architecture:
Client (Browser)
    |
    |--> Users Server: https://educore-m9yh.onrender.com/
    |
    |--> Courses/Enrollments Server: https://educore-subscriptions-db.onrender.com/
    |
    v
MongoDB Atlas

Authentication Flow:
1. User logs in through the Users Server.
2. Password is validated using bcrypt.
3. Server returns a JWT token.
4. Token is stored in sessionStorage.
5. All protected fetch requests include:
   Authorization: Bearer <token>

Important API Routes:

Users Server (https://educore-m9yh.onrender.com/):
POST /login
POST /register
GET /users
PATCH /users/<id>
DELETE /users/<id>

Courses & Enrollments Server (https://educore-subscriptions-db.onrender.com/):
GET /courses
POST /courses
PATCH /courses/<id>
DELETE /courses/<id>

GET /students
POST /students
PATCH /students/<id>
DELETE /students/<id>

GET /enrollments
POST /enrollments
PATCH /enrollments/<id>
DELETE /enrollments/<id>

Project Folder Structure (based on your actual tree):
project_4
    README.md
    backend/
        new_users_folder/
            controllers/
            data/
            main/
            repositories/
            services/
        subscriptions_DB/
            clients/
            controllers/
            data/
            main/
            repositories/
            services/
    docs/
        index.html
        frontend/
            addCourse.html
            addEnrolled.html
            addUser.html
            alerts.js
            allCourses.html
            allEnrolled.html
            auth.js
            coplot.html
            courses.html
            CreateAccount.html
            css.css
            editCourse.html
            editStudent.html
            editUser.html
            enrollments.html
            jpt.html
            login.html
            main.html
            manageUsers.html
            navbarAndName.js
            style.css
            users.html

Installation (Local development – optional):
Only needed if someone wants to run the project locally.

Users Server:
cd backend/new_users_folder/main
pip install -r ../requirements.txt
python app.py

Courses/Enrollments Server:
cd backend/subscriptions_DB/main
pip install -r ../requirements.txt
python app.py

Frontend:
Open the HTML files inside docs/frontend in a browser OR serve using any static server.

Author:
Rivka Shvartz
Full Stack Developer (Python, Flask, JavaScript, MongoDB)
GitHub: https://github.com/RIVKI-SHVARTS

Summary:
EduCore is a complete multi-server management system built with two Flask backends and a fully deployed web-based frontend. The project demonstrates secure authentication, multi-service architecture, cloud deployment and practical full-stack development skills.
