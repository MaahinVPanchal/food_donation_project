# 🚀FoodBridgeNgo Project

## ✨Requirements: -
- Python 3.x
- asgiref==3.8.1
- Django==5.0.7
- sqlparse==0.5.1
- tzdata==2024.1

After requirements are fullfilled you need to learn basic commands which are useful in django 

![image](https://github.com/user-attachments/assets/fe6f48e6-5dc7-48fb-b747-043397ae0b21)

## ➡️Installation Guide

### Globally Installing django
```bash
    pip install django
    django-admin startproject projectname
    cd projectname
    python manage.py runserver
```
- Uninstall 
```bash
    pip uninstall django
```

### Separate environment for installing django
```bash
    pip install virtualenvwrapper-win
    mkvirtualenv nameofvirtualenv
    workon nameofvirtualenv
    pip install django
    django-admin --version
    django-admin startproject projectname
    cd projectname
    python manage.py runserver
```
- Uninstall django 
```bash
    pip uninstall django
    rmvirtualenv envname
    pip uninstall virtualenvwrapper-win
```

### Some Migrations Commands
```bash
python manage.py showmigrations
python manage.py makemigrations
python manage.py sqlmigrate enroll0001
python manage.py migrate
```

### Create Superuser
```bash
python manage.py createsuperuser
```
## Project Workflow
1. ### Start with Small Tasks:
   Begin by linking a few HTML pages in Django and verify their connection by running the server.
2. ### Plan Your Large Project:
   Create a flowchart to outline your approach for developing the entire project.

## 🤩Understanding What you have to add in my project to run

- At first You need to add your own .env file in food_donation_project like
- ```bash
      EMAIL_HOST_USER=local@gmail.com
      EMAIL_HOST_PASSWORD=your credential passkey
      PASSWORD1=password1
      PASSWORD2=password2
      PASSWORD3=password3
  ```
  Where you need to create an gmail account for smtp service and add password to login for volunteer
- Open terminal and go to path and then write code
- ```bash
      python manage.py runserver
  ```

- Now it will run on localhost 8000 and view all pages
![Screenshot 2024-08-01 224814](https://github.com/user-attachments/assets/228d3526-7381-4733-bd78-0da8dab8d428)

## 😊Demo of my website

https://github.com/user-attachments/assets/def64c5b-283a-4399-8464-54382f115f47


