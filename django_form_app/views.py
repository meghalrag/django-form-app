# django_form_app/views.py
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact

def home(request):
    # Render the elegant home page
    return render(request, 'home.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            contact = Contact(name=data['name'], email=data['email'], phone=data['phone'])
            contact.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')

def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'list_entries.html', {'contacts': contacts})
