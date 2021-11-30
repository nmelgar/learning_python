from django.contrib import admin

from.models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    #fields to display in the listing display in admin
    list_display = ['name', 'species', 'breed', 'age', 'sex']