from django.urls import path
#from django.conf.urls import patterns, url
#from django.conf.urls import url
from django.views.generic import TemplateView
from breeze import views

app_name = "main"

urlpatterns = [
    path("", views.create_account, name="create_account"),
    path("home/", views.home, name="home"),
    path("log_in/", views.login, name="login"),
    path("password_reset", views.password_reset_request, name="password_reset"),
]
