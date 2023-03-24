from django.shortcuts import render
from jobs.models import Job
from projects.models import Project

def home(request):
    jobs = Job.objects
    projects = Project.objects.all().order_by('id')[:3]
    return render(request, 'main/home.html', {'jobs': jobs, 'projects': projects})
