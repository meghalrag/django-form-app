# django_form_app/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=100, required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=10, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))  # Added phone number field
