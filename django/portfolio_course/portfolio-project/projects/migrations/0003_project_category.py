# Generated by Django 4.1.7 on 2023-03-23 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('Web Dev', 'Web Dev'), ('Data', 'Data')], default='Web Dev', max_length=10),
        ),
    ]
