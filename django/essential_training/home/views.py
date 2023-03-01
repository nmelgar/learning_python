from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here
#everytime this function receives a request
#it will return what's in tht return
def home(request):
    return HttpResponse('hello world')
