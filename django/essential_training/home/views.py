from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

#everytime this function receives a request
#it will return what's in tht return
class HomeView(TemplateView):
    template_name = 'home/welcome.html'


class AuthorizedView(TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'

 