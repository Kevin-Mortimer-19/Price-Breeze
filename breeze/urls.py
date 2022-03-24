from django.urls import path
#from django.conf.urls import patterns, url
#from django.conf.urls import url
from django.views.generic import TemplateView
from breeze import views

urlpatterns = [
    path("", views.home, name="home"),
    path("", views.login, name="login"),
    path("", views.create_account, name="create_account"),
]

"""urlpatterns += patterns('breeze.views',
   url(r'^connection/',TemplateView.as_view(template_name = 'login.html')),
   url(r'^login/', 'login', name = 'login'))"""