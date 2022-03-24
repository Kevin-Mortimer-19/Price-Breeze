from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from breeze.forms import LoginForm, CreateForm
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic

def create_account(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created.")
            return redirect("home")
        else:
            messages.error(request, "Account creation failed again.")
    else:
        form = CreateForm()
    return render(request, 'account_creation.html', {'form':form})

def log_in(request):
   return render(request, 'login.html')

def home(request):
    return render(request, "home_page.html")
