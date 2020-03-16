from django.contrib import admin

from .models import Project

# Register your models here.


#  Use https://github.com/yourlabs/django-autocomplete-light for autocomplete of admin forms


# Fields to show from models
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('repository_id', 'study_title', 'country', 'disease')
    #  list_display_links = ('id', 'title')
    search_fields = ('study_title', 'country')
    list_per_page = 10



# Registering the models
admin.site.register(Project, ProjectAdmin)
