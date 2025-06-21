# Tailwebs 
# Teacher Portal – Student Record Management System

A simple Django-based web application that allows teachers to **register**, **login**, and **manage student records** — including adding, editing, and deleting entries. This project uses Bootstrap for responsive UI and Django's built-in authentication system.

---

##  Features

-  User registration with password validation (min 7 characters, number & symbol required)
-  Secure user login/logout
-  Add student records (Name, Subject, Mark)
- Edit and update student records via Bootstrap modals
-  Delete student records
-  Flash messages for success & error feedback
-  Toast notifications for clean UI feedback

---

##  Tech Stack

- **Backend:** Django 5.x
- **Frontend:** HTML5, Bootstrap 5.3 , CSS ,JavaScript
- **Database:** SQLite3 (default)
- **Language:** Python 3.11+

---

##  Setup Instructions

**Clone the repository:**

```bash
git clone https://github.com/your-username/teacher-portal.git
cd teacher-portal

Create virtual environment and activate it:

python -m venv env
source env/bin/activate 

Install dependencies:

pip install -r requirements.txt


Apply migrations:

python manage.py makemigrations
python manage.py migrate


Run the development server:

python manage.py runserver

Open browser:

http://127.0.0.1:8000/
