from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
   user = forms.CharField(max_length=100)
   password = forms.CharField(widget=forms.PasswordInput())

   def clean_message(self):
      username = self.cleaned_data.get("username")
      dbuser = User.objects.filter(name=username)

      if not dbuser:
         raise forms.ValidationError("User does not exist in the database")
      return username


class CreateForm(UserCreationForm):

   def clean_message(self):
      username = self.cleaned_data.get("username")
      dbuser = not User.objects.filter(name=username)

      if dbuser:
         raise forms.ValidationError("User already exists in the database")
      return username

   def save(self, commit=True):
      user = super(CreateForm, self).save(commit=False)
      if commit:
         user.save()
      return user
