from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index),                  # In and out
    path('logout', views.logout),
    path('loading', views.renderDash),
                                            # add comments and replies
    path('add_comment/<str:book_title>/<int:page_no>', views.add_comment),
                                            # Renders
    path('all_comments', views.allcommies),
    path('wip', views.wip),
    path('submit', views.submit),
                                            #Forms
    path('register', views.register),
    path('login', views.login),
    path('submitPage', views.submitPage),
    path('createComic', views.createComic),
    path('viewpage/<str:book_title>/<int:page_no>', views.viewPage),
    path('add_like/<int:id>', views.addLikes),
    # path('bookmark/<int:id>', views.bookmark),
    path('delete', views.delete),
    path('deleteCom/<int:id>', views.deleteCom),
    path('next_page/<int:id>', views.nextPage),
    path('deletepage/<str:book_title>/<int:page_no>', views.deletePage),
]