from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_view),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('home', views.home, name='home'),
    # path('gallery', views.gallery, name='gallery'),
    # path('my_posts', views.my_posts, name='my_posts'),
]
