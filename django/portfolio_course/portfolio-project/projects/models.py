from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100, default="Project Name")
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    url = models.CharField(max_length=400)
    source_code = models.CharField(max_length=400)
    CATEGORY_CHOICES = [
        ('Web Dev', 'Web Dev'),
        ('Data', 'Data'),
    ]
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='Web Dev')