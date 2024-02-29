from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='index'),
    path("explore/", views.explore, name='explore'),
    path("author/", views.author, name='author'),
    path("create/", views.create, name='create'),

    path("login/", views.login_view, name='login'),
    path("register/", views.register, name='register'),
]
