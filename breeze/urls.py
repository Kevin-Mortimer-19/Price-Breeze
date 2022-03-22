from django.urls import path
from breeze import views

urlpatterns = [
    path("", views.home, name="home"),
]