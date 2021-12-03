from django.db import models

class Job(models.Model):
    #images
    #property with a image field
    images = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
