from django.shortcuts import render
from breeze.forms import LoginForm

def home(request):
    return render(request, 'account_creation.html')

def login(request):
   username = "not logged in"
   
   if request.method == "POST":
      
      MyLoginForm = LoginForm(request.POST)
      
      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
   else:
      MyLoginForm = LoginForm()
		
   return render(request, 'loggedin.html', {"username" : username})