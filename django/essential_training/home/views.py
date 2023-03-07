from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here
#everytime this function receives a request
#it will return what's in tht return
class HomeView(TemplateView):
    template_name = 'home/welcome.html'


class AuthorizedView(TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'

 