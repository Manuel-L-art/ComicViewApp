from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index),                  # In and out
    path('logout', views.logout),
    path('loading', views.renderDash),
                                            # add comments and replies
    path('add_comment', views.add_comment),
                                            # Renders
    path('all_comments', views.allcommies),
    path('wip', views.wip),
    path('submit', views.submit),
                                            #Forms
    path('register', views.register),
    path('login', views.login),
    path('submitPage', views.submitPage),
    path('createComic', views.createComic),
    path('viewComicPage/<int:page_id>', views.viewComic),
    path('add_like/<int:id>', views.addLikes),
    path('bookmark/<int:id>', views.bookmark),
]