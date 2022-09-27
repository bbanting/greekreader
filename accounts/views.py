from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView



class Login(LoginView):
    redirect_authenticated_user = False
    template_name = "api/login.html"


class Logout(LogoutView):
    ...