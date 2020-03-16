from django.db import models
from taggit.managers import TaggableManager

# https://stackoverflow.com/questions/2459979/how-to-import-csv-data-into-django-models


class Project(models.Model):
    repository_id = models.CharField(max_length=20) # max length was 11
    study_title = models.CharField(max_length=410) # max length was 308
    study_link = models.CharField(max_length=150) # max length was 108
    assay_type = models.CharField(max_length=20) # max length was 9
    technology = models.CharField(max_length=20) # max length was 11
    country = models.CharField(max_length=60) # max length was 41
    disease = models.CharField(max_length=100) # max length was 75
    study_design = models.CharField(max_length=80) # max length was 55
    body_site = models.CharField(max_length=50) # max length was 31
    platform = models.CharField(max_length=40) # max length was 28
    participant_features = models.CharField(max_length=280) # max length was 212
    library_layout = models.CharField(max_length=10) # max length was 7
    lon_lat = models.CharField(max_length=50) # max length was 32
    sample_type = models.CharField(max_length=30) # max length was 22
    collection_date = models.CharField(max_length=30) # max length was 21
    ethnicity = models.CharField(max_length=110) # max length was 84
    urbanzation = models.CharField(max_length=20) # max length was 13
    region = models.CharField(max_length=150) # max length was 108
    city = models.CharField(max_length=60) # max length was 44
    target_amplicon = models.CharField(max_length=50) # max length was 31
    diet = models.CharField(max_length=180) # max length was 136
    sample_number = models.PositiveSmallIntegerField() # min: 1, max: 894, mean: 6.519581056466302
    tags = TaggableManager(help_text=None)
    def __str__(self):
        return self.study_title
