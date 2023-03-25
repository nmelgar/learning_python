from django.shortcuts import render
from jobs.models import Job
from projects.models import Project


def home(request):
    jobs = Job.objects
    # filter to display the first 3 items reference https://docs.djangoproject.com/en/dev/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    # projects = Project.objects.all().order_by('id')[:3]
    projects = Project.objects.all().order_by('?')[:3]
    return render(request, 'main/home.html', {'jobs': jobs, 'projects': projects})
