from django.shortcuts import render
from . models import Project

def projectsDisplay(request):
    projects = Project.objects
    return render(request, 'projects/projects.html', {'projects': projects})
