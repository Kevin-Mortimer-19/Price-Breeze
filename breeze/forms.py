from django import forms
from breeze.models import Dreamreal


class LoginForm(forms.Form):
   user = forms.CharField(max_length=100)
   password = forms.CharField(widget=forms.PasswordInput())

   def clean_message(self):
      username = self.cleaned_data.get("username")
      dbuser = Dreamreal.objects.filter(name=username)

      if not dbuser:
         raise forms.ValidationError("User does not exist in the database")
      return username


class CreateForm(forms.Form):
   user = forms.CharField(max_length=100)
   password = forms.CharField(widget=forms.PasswordInput())

   def clean_message(self):
      username = self.cleaned_data.get("username")
      dbuser = not Dreamreal.objects.filter(name=username)

      if dbuser:
         raise forms.ValidationError("User already exists in the database")
      return username
