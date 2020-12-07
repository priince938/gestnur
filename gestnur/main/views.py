from django.shortcuts import render,redirect
from .forms import ContactForm
from .models import Contact
from django.contrib import messages
# Create your views here.

def Home(request):
    return render(request,'main/index.html')


def product(request):
    return render(request,'main/portfolio.html')

def about(request):
    return render(request,'main/about.html')

def service(request):
    return render(request,'main/services.html')

def team(request):
    return render(request,'main/team.html')

def contact(request):

    if request.method == 'POST':
        form_set = ContactForm(request.POST)
        if form_set.is_valid():

           data = form_set.cleaned_data
           contact=Contact(name=data['name'],email=data['email'],phone=data['phone'],subject=data['subject'],message=data['message'])
           contact.save()
           messages.info(request, "Thank you,We Will contact you soon")

        else:
            messages.warning(request,"Ther is some problem please direct call on the provided Number")
    context={
        'form':ContactForm
    }
    return render(request,'main/contact.html',context)