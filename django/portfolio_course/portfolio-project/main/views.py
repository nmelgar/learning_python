from django.shortcuts import render
from jobs.models import Job
from projects.models import Project

def home(request):
    jobs = Job.objects
    projects = Project.objects
    return render(request, 'main/home.html', {'jobs': jobs, 'projects': projects})

