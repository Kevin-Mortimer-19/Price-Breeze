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
		
   return render(request, 'home_page.html', {"username" : username})


def create_account(request):
   if request.method == "POST":

   MyCreateForm = CreateForm(request.POST)

   if MyCreateForm.is_valid():
      MyCreateForm.save()
   else:
      MyCreateForm = CreateForm()

   return render(request, 'homepage.html', {"username" : username})