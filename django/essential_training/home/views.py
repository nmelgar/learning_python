from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here
#everytime this function receives a request
#it will return what's in tht return
def home(request):
    return render(request, 'home/welcome.html', {})

@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {})