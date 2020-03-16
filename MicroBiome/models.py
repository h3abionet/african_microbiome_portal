from django.db import models
from taggit.managers import TaggableManager

# https://stackoverflow.com/questions/2459979/how-to-import-csv-data-into-django-models


class Project(models.Model):
    repository_id = models.CharField(
        max_length=20, null=False, blank=False, default=False)  # max length was 11
    # min: 1, max: 1729, mean: 234.77777777777777
    sample_count = models.PositiveSmallIntegerField(
        null=False, blank=False, default=False)
    # max length was 208; (!) contains 3 Nones (11.11%)
    study_title = models.CharField(max_length=280, default=False)
    # max length was 10; (!) contains 26 Nones (96.30%)
    study_link = models.CharField(max_length=20, default=False)
    # max length was 9; (!) contains 1 Nones (3.70%)
    assay_type = models.CharField(max_length=20, null=True)
    platform = models.CharField(max_length=20)  # max length was 11
    # max length was 41; (!) contains 1 Nones (3.70%)
    country = models.CharField(max_length=60, null=True)
    disease = models.CharField(max_length=100, null=True)  # max length was 75
    # max length was 15; (!) contains 4 Nones (14.81%)
    study_design = models.CharField(max_length=20, null=True)
    body_site = models.CharField(max_length=30, null=True)  # max length was 21
    # (!) contains 5 Nones (18.52%); min: -33.928992, max: 35.0, mean: -0.7330072363636365
    lon = models.FloatField(null=True)
    # (!) contains 5 Nones (18.52%); min: -16.5667, max: 39.742359, mean: 22.202148209090918
    lat = models.FloatField(null=True)
    repo = models.CharField(max_length=10, null=True)  # max length was 7
    sample_type = models.CharField(
        max_length=30, null=True)  # max length was 22
    tags = TaggableManager( help_text=None )
    def __str__(self):
        return self.study_title
