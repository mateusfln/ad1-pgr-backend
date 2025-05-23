from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("perguntasfrequentes", views.perguntasfrequentes, name="perguntasfrequentes"),
    path("funcionalidades", views.funcionalidades, name="funcionalidades"),
]