Django CRUD Application – Project Documentation

Overview
This project is a simple Student Management System built using Django. It performs full CRUD
operations:- Create Student- Read Students- Update Student- Delete Student
Purpose: Learn Django Models, Views, Templates, Forms, URLs, and Admin.
Tech Stack- Python 3- Django 5- SQLite 3- HTML- CSS

Setup Instructions
1. Create Virtual Environment:
python -m venv venv
2. Activate:
Windows: venv\Scripts\activate
Linux/Mac: source venv/bin/activate
3. Install Django:
pip install django
4. Create Project:
django-admin startproject myproject
5. Create App:
python manage.py startapp students
Model (Student)
name = CharField
email = EmailField
age = IntegerField
course = CharField
Run Migrations:
python manage.py makemigrations
python manage.py migrate
Forms (StudentForm)
Uses Django ModelForm for handling form creation and validation.
CRUD Views- student_list: Shows all students- add_student: Adds new student- edit_student: Updates student- delete_student: Removes student
URL Configurations
Includes URL patterns for list, add, edit, and delete.
Templates
index.html, add_student.html, edit_student.html used for UI rendering.
Admin Panel
Register model:
admin.site.register(Student)
Create superuser:
python manage.py createsuperuser
Conclusion
This project demonstrates Django MVT, database modeling, template rendering, form handling and
CRUD operations
