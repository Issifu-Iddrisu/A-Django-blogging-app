from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .models import Tutorial
import datetime



# Create your views here.
def homepage(request):
    return render(request, 'main/home.html',{"tutorials":Tutorial.objects.all()} )
    

def newyear(request):
    date =  datetime.datetime.now()
    return render(request, 'main/newyear.html', {'date': date.month == 1 and date.year == 1})


def signup(request):
    if request.method  == "POST":
        form  = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main:login")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = UserCreationForm()
    return render(request, "main/signup.html", {"form":form})


def login_to(request):
    form = AuthenticationForm()
    return render(request, "main/login.html", {"form":form})
 

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out sucessfully")
    return redirect("main:homepage")