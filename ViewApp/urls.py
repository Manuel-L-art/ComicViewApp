from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path(r'^password/$', views.edit),
]