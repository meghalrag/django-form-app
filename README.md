# django-ec2-app

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

- run

```
 gunicorn --bind 0.0.0.0:8080 django_form_app.wsgi:application 
```

