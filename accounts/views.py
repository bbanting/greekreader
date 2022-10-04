from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView



class Login(LoginView):
    redirect_authenticated_user = False
    template_name = "api/login.html"
    next_page = "http://localhost:8000" # Whatever the url of the main front end is


class Logout(LogoutView):
    next_page = "login"