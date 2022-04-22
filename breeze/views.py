from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from breeze.forms import LoginForm, CreateForm, addToList
from breeze.models import ShoppingList, Item
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic


from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages


from django.shortcuts import HttpResponse
from breeze.open_json import *


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
        search_results = startTableAlt()
    return render(request, "home_page.html", {"form":form, "results": search_results})

def log_in(request):
   return render(request, 'login.html')

def home(request):
	if request.method == "POST":
		form = addToList(request.POST)
		if form.is_valid():
			list = ShoppingList.objects.get(userid=request.user)
			name = request.POST.get('item')
			item = Item(userid=list, item_name=name, item_id = 1)
			item.save()
	else:
		form = addToList()
	return render(request, "home_page.html", {"form":form})


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
                    
					return redirect ("password_reset/done/")
    
	password_reset_form = PasswordResetForm()

	return render(request=request, template_name="password/password_reset.html", context={"password/password_reset_form":password_reset_form})

def list(request):
	list = ShoppingList.objects.get(userid=request.user)
	items = Item.objects.filter(userid=list)
	return render(request, "shopping_list.html", {"item_list":items})

def password_change_form(request):
     form = PasswordChangeForm(request.POST)
     return render(request, "password_reset_confirm.html")


#table output views for sorting urls


def table(request):
#initial table
	output = startTable()
	return render(request, 'home_page.html', {'data':output})

#price tables
def tableSortHPrice(request):
#most to least
	output = highTablePrice()
	return render(request, 'home_page.html', {'data':output})

def tableSortLPrice(request):
#least to most
	output = lowTablePrice()
	return render(request, 'home_page.html', {'data':output})


#product name tables
def tableSortHName(request):
#Z to A
	output = highTableName()
	return render(request, 'home_page.html', {'data':output})

def tableSortLName(request):
#A to Z
	output = lowTableName()
	return render(request, 'home_page.html', {'data':output})


#store name tables
def tableSortHStore(request):
#Z to A
	output = highTableStore()
	return render(request, 'home_page.html', {'data':output})

def tableSortLStore(request):
#A to Z
	output = lowTableStore()
	return render(request, 'home_page.html', {'data':output})