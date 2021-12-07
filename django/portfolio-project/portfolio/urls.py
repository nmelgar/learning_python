
from django.contrib import admin
from django.urls import path
import jobs.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #when someone types /admin, he will be taken to admin
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
