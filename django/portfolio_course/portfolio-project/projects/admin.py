from django.contrib import admin


from . models import Project

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Project, PortfolioAdmin)