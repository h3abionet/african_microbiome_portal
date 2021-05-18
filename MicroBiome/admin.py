from django.contrib import admin

from .models import (TestProject, Pubmed, LocEthDiet, Platform, Disease,
                     Amplicon, Assay, Samples)

# Register your models here.


#  Use https://github.com/yourlabs/django-autocomplete-light for autocomplete of admin forms


# Fields to show from models
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('repoid', 'title')
    #  list_display_links = ('id', 'title')
    search_fields = ('repoid','title')
    list_per_page = 10

class PubmedAdmin(admin.ModelAdmin):
    list_display = ('pubid', 'title')
    search_fields = ('pubid', 'title')
    list_per_page = 10
    
class LocEthDietAdmin(admin.ModelAdmin):
    list_display = ('country', 'region', 'urbanization', 'cityvillage',
                    'ethnicity', 'diets', 'lon', 'lat')
    search_fields = ('country', 'region', 'urbanization', 'cityvillage',
                    'ethnicity', 'diets', 'lon', 'lat')
    list_per_page = 10


class PlatformAdmin(admin.ModelAdmin):
    list_display = ('platform',)
    search_fields = ('platform',)
    list_per_page = 10

class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('disease', "doid")
    search_fields = ('disease',)
    list_per_page = 10


class AmpliconAdmin(admin.ModelAdmin):
    list_display = ('amplicon',)
    search_fields = ('amplicon',)
    list_per_page = 10


class AssayAdmin(admin.ModelAdmin):
    list_display = ('assay',)
    search_fields = ('assay',)
    list_per_page = 10

class SamplesAdmin(admin.ModelAdmin):
    list_display = ('sampid', 'avspotlen', 'coldate')
    search_fields = ('sampid', 'avspotlen', 'coldate')
    list_per_page = 10


# Registering the models
# admin.site.register(Project, ProjectAdmin)
admin.site.register(TestProject, ProjectAdmin)
admin.site.register(Pubmed, PubmedAdmin)
admin.site.register(Disease, DiseaseAdmin)
admin.site.register(Assay, AssayAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(LocEthDiet, LocEthDietAdmin)
admin.site.register(Amplicon, AmpliconAdmin)
admin.site.register(Samples, SamplesAdmin)

