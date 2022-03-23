from django.urls import path
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from breeze import views

urlpatterns = [
    path("", views.home, name="home"),
]

urlpatterns = patterns('breeze.views',
   url(r'^connection/',TemplateView.as_view(template_name = 'login.html')),
   url(r'^login/', 'login', name = 'login'))