
from django.contrib import admin
from django.urls import path

import jobs.views

urlpatterns = [
    #when someone types /admin, he will be taken to admin
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),
]
