from django.urls import path
#from django.conf.urls import patterns, url
#from django.conf.urls import url
from django.views.generic import TemplateView
from breeze import views



urlpatterns = [
    path("", views.create_account, name="create_account"),
    path("home/", views.home, name="home"),
    path("log_in/", views.login, name="login"),
    path("password_reset", views.password_reset_request, name="password_reset_request"),
    # path('search_results', views.home, name="search_results_req"),
    path("list/", views.list, name="list"),

    #sorting urls
    path("high_price/", views.tableSortHPrice, name="highPrice"),
    path("low_price/", views.tableSortLPrice, name="lowPrice"),
    path("high_name/", views.tableSortHName, name="highName"),
    path("low_name/", views.tableSortLName, name="lowName"),
    path("high_store/", views.tableSortHStore, name="highStore"),
    path("low_store/", views.tableSortLStore, name="lowStore"),
    path("reset/", views.table, name="reset")
]
