
# EduCore – Course, Users & Enrollment Management System

EduCore is a full-stack web management system built with a **multi-service Flask backend** and a **fully deployed HTML/CSS/JavaScript frontend**.

The system provides secure management of **Users, Courses, Students and Enrollments**, including authentication, authorization and full CRUD functionality.

---

## 🌐 Live Demo

**Frontend:**  
https://educore-frontend.netlify.app/

**Users Server (Auth & Users):**  
https://educore-m9yh.onrender.com/

**Courses & Enrollments Server:**  
https://educore-subscriptions-db.onrender.com/

---

## 🔐 Demo Login (Read-Only)

username: demo
password: Demo1234

markdown
Copy code

The demo user has limited permissions and cannot modify or delete data.

---

## 🧩 Architecture Overview

- **Two independent Flask REST API servers**
- **Frontend communicates directly with both servers**
- **MongoDB Atlas** used for persistent storage
- **JWT-based authentication**
- **bcrypt password hashing**

Client (Browser)
|--> Users Server (Render)
|--> Courses & Enrollments Server (Render)
v
MongoDB Atlas

yaml
Copy code

---

## ⚙️ Main Features

- Multi-service backend architecture
- Secure login with bcrypt + JWT
- Role-based permissions
- Full CRUD: Users, Courses, Students, Enrollments
- RESTful API design
- Cloud deployment (Render, Netlify, MongoDB Atlas)
- Clean project structure (controllers / services / repositories)
- Responsive and interactive frontend

---

## 🔑 Authentication Flow

1. User logs in via Users Server  
2. Password validated with bcrypt  
3. JWT token returned  
4. Token stored in `sessionStorage`  
5. All protected requests use:

Authorization: Bearer <token>

yaml
Copy code

---

## 📌 Key API Endpoints

### Users Server
- POST `/login`
- POST `/register`
- GET `/users`
- PATCH `/users/<id>`
- DELETE `/users/<id>`

### Courses & Enrollments Server
- `/courses`
- `/students`
- `/enrollments`
(Full CRUD supported)

---

## ⚠️ Deployment Note (Free Tier Hosting)

This project is deployed on **free cloud tiers** (Render & MongoDB Atlas).

The **first request after inactivity may take a few seconds** due to cold start.  
Once active, the system runs normally.

The architecture is **production-ready** and can be easily migrated to a paid environment for higher performance and scalability.

---

## 👩‍💻 Author

**Rivka Shvartz**  
Full Stack Developer (Python, Flask, JavaScript, MongoDB)  
GitHub: https://github.com/RIVKI-SHVARTS

---

## 📘 Summary

EduCore demonstrates real-world full-stack development with secure authentication, multi-service backend architecture and full cloud deployment.