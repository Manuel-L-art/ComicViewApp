from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    # path('edit', views.edit),
    
    # add comments and replies
    path('add_comment', views.add_comment),
]