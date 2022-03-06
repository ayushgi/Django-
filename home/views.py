from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable1":"My name is Ayush Raj",
        "variable2":"I am a great person"
    }
    return render(request,'base.html',context)

def about(request):
    return HttpResponse("this is about page")   

def services(request):
    return HttpResponse("this is services page") 

def contact(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        opinion=request.POST.get('opinion')
        contact=Contact(name=name, email=email,opinion=opinion,date=datetime.today())
        contact.save()
        messages.success(request,'Form has been submitted successfully')
    return render(request,'contact.html')


    # python manage.py startapp [app ka name likho] (home)
    # python manage.py runserver to run server