from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    # path('edit', views.edit),
    
    # add comments and replies
    path('add_comment', views.add_comment),
    path('all_comments', views.allcommies),
    path('logout', views.logout),
    path('wip', views.wip),
    path('submit', views.submit),
    path('submitPage', views.submitPage),
    path('createComic', views.createComic),
    path('viewComicPage/<int:page_id>', views.viewComic),
]