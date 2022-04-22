from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from breeze.forms import *
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
from breeze.shops import *


# View for creating an account
# Defines the response to form submission and renders the page
def create_account(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            list = ShoppingList(userid=user)
            list.save()
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

# View for the home/search page
# defines responses to search inputs and add button interactions
def home(request):
	form = searchFor()
	if request.method == "POST":
		if 'add_to_list' in request.POST:
			saveItem(request)
		if 'searchInput' in request.POST:
			form = searchFor(request.POST)
			if form.is_valid():
				productItem = request.POST.get('product')
				scrape_product(productItem)
		else:
			form = searchFor()
	output = startTable()
	return render(request, "home_page.html", {'results': output, 'form': form})


# Allows the password reset form to take input from user in the 
# form of an email and sends an email to the user containing the link to reset password
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

	return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})

# View for handling the shopping list page
# Handles a form submission from the search page, and displays a User's ShoppingList
def list(request):
	list = ShoppingList.objects.get(userid=request.user)
	if request.method == "POST":
		name = request.POST.get('title')
		new_item = Item(userid=list, item_name=name, item_id = 1)
		new_item.save()
	items = Item.objects.filter(userid=list)
	return render(request, "shopping_list.html", {"item_list":items})

# View for changing password
def password_change_form(request):
     form = PasswordChangeForm(request.POST)
     return render(request, "password_reset_confirm.html")

# View for  showing the user profile
def user_profile_view(request):
     user_profile_form = UserProfileForm(request.POST)
     return render(request, "user_profile.html",{'user_profile_form':user_profile_form})


#table output views for sorting urls
def table(request):
#initial table
	output = startTable()
	return render(request, 'home_page.html', {'results':output})

#price tables
def tableSortHPrice(request):
#most to least
	if request.method == "POST":
		if 'add_to_list' in request.POST:
			saveItem(request)
	output = highTablePrice()
	form = searchFor()
	return render(request, 'home_page.html', {'results':output, 'form':form})

def tableSortLPrice(request):
    #least to most
	if request.method == "POST":
		if 'add_to_list' in request.POST:
			saveItem(request)
	output = lowTablePrice()
	form = searchFor()
	return render(request, 'home_page.html', {'results':output, 'form':form})

#product name tables
def tableSortHName(request):
#Z to A
	if request.method == "POST":
		if 'add_to_list' in request.POST:
			saveItem(request)
	output = highTableName()
	form = searchFor()
	return render(request, 'home_page.html', {'results':output, 'form':form})

def tableSortLName(request):
#A to Z
	if request.method == "POST":
		if 'add_to_list' in request.POST:
			saveItem(request)
	output = lowTableName()
	form = searchFor()
	return render(request, 'home_page.html', {'results':output, 'form':form})

#store name tables
def tableSortHStore(request):
#Z to A
	if request.method == "POST":
		if 'add_to_list' in request.POST:
			saveItem(request)
	output = highTableStore()
	form = searchFor()
	return render(request, 'home_page.html', {'results':output, 'form':form})

def tableSortLStore(request):
#A to Z
	if request.method == "POST":
		if 'add_to_list' in request.POST:
			saveItem(request)
	output = lowTableStore()
	form = searchFor()
	return render(request, 'home_page.html', {'results':output, 'form':form})

def saveItem(request):
	list = ShoppingList.objects.get(userid=request.user)
	name = request.POST.get('title')
	this_price = request.POST.get('price')
	this_location = request.POST.get('location')
	new_item = Item(userid=list, item_name=name, item_id = 1, location=this_location, price=this_price)
	new_item.save()