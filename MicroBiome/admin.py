from django.contrib import admin

from .models import Pubmed, Samples, Platform, LocEthDiet, Disease, BodySite, BioProject


# Register your models here.


#  Use https://github.com/yourlabs/django-autocomplete-light for autocomplete of admin forms


# Fields to show from models
class BioProjectAdmin(admin.ModelAdmin):
    list_display = ('repoid',)
    #  list_display_links = ('id', 'title')
    search_fields = ('repoid',)
    list_per_page = 10
#


class PubmedAdmin(admin.ModelAdmin):
    list_display = ("pubid", "title")
    search_fields = ("pubid", "title")
    list_per_page = 10


class BodySiteAdmin(admin.ModelAdmin):
    list_display = ('bodysite',)
    search_fields = ('bodysite',)
    list_per_page = 10


#
class LocEthDietAdmin(admin.ModelAdmin):
    list_display = ('country', 'region', 'urbanization', 'cityvillage',
                    'ethnicity', 'diets')
    search_fields = ('country', 'region', 'urbanization', 'cityvillage',
                     'ethnicity', 'diets')
    list_per_page = 10
#
#


class PlatformAdmin(admin.ModelAdmin):
    list_display = ('technology', 'platform', 'assay')
    search_fields = ('technology', 'platform', 'assay')
    list_per_page = 10


class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('disease', "doid")
    search_fields = ('disease',)
    list_per_page = 10
#
#
# class AmpliconAdmin(admin.ModelAdmin):
#     list_display = ('amplicon',)
#     search_fields = ('amplicon',)
#     list_per_page = 10
#
#
# class AssayAdmin(admin.ModelAdmin):
#     list_display = ('assay',)
#     search_fields = ('assay',)
#     list_per_page = 10
#


class SamplesAdmin(admin.ModelAdmin):
    filter_horizontal = ('pubmed', 'disease',)
    list_display = ('sampid', 'avspotlen', 'platform', 'bodysite',)
    search_fields = ('sampid', 'avspotlen', 'platform',
                     'bodysite', 'disease', "pubmed",)
    list_per_page = 10


#
#
# # Registering the models
admin.site.register(BioProject, BioProjectAdmin)
# admin.site.register(TestProject, ProjectAdmin)
admin.site.register(Pubmed, PubmedAdmin)
admin.site.register(Disease, DiseaseAdmin)
admin.site.register(BodySite, BodySiteAdmin)
# admin.site.register(Assay, AssayAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(LocEthDiet, LocEthDietAdmin)
# admin.site.register(Amplicon, AmpliconAdmin)
admin.site.register(Samples, SamplesAdmin)
#
