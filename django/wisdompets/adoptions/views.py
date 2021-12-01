from django.shortcuts import render
from django.http import Http404
#import pet class
from .models import Pet

def home(request):
    pets = Pet.objects.all()
    #renders html to the templates
    #render requires templates to work
    #1st argument request object | 2 string with template name we want to use
    return render(request, 'home.html', {
        #dictionary with data to be available in the template
        #key
        'pets': pets,
    })


def pet_detail(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found')
    return render(request, 'pet_detail.html', {
        'pet': pet,
    })
