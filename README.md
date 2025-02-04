# Django Contacts Storage app

- pip install django mongoengine gunicorn

- django-admin startproject django_form_app

- configure mongoengine in settings.py
```
import mongoengine
# MongoEngine connection configuration:
mongoengine.connect(
    db='django_form_app_db',   # Replace with your database name if needed
    host='localhost',  # Replace with your MongoDB host if different
    port=27017         # Replace with your MongoDB port if needed
)
```

# App Setup Guide

Step 1: Clone the repo
```
git clone https://github.com/meghalrag/django-form-app.git
```
Step 2: Create a virtual environment to run the app
``` 
python3 -m venv ec2_env 
```
Step 3: Activate Environment
```
source ec2_env/bin/activate
```
Step 4: Go to the project folder
```
cd django-form-app/
```
step 5: install project dependencies packages using pip and requirements.txt
```
pip install -r requirements.txt
```
Step 6: Start Mongodb service
```
sudo service mongod start
```
Step 7: Run application
```
python manage.py runserver 0:8000
```


