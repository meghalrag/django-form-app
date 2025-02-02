# django_form_app/models.py
from mongoengine import Document, StringField

class Contact(Document):
    name = StringField(required=True, max_length=100)
    email = StringField(required=True, max_length=100)
    phone = StringField(required=True, max_length=10)
