#!/usr/bin/env python3
from django.db import models
from datetime import date
from taggit.managers import TaggableManager

# https://stackoverflow.com/questions/2459979/how-to-import-csv-data-into-django-models

# https://stackoverflow.com/questions/21512647/how-to-count-the-amount-of-objects-in-a-django-joined-table

date_default = date(1, 1, 1)

# NOTE: l2 > link to


class RawData(models.Model):
    """This class is to store data in raw format and allowing people to
    download the query result. Data is complex that why this class has been
    created. In future, it might be remove"""

    repoid = models.CharField(max_length=100,
                              unique=False,
                              null=False,
                              blank=False)
    sample_size = models.IntegerField(default=0, null=False, blank=False)
    pubid = models.CharField(max_length=20,
                             unique=False,
                             null=False,
                             blank=False)
    # doi = models.CharField(max_length=100, unique=True, blank=False)
    title = models.CharField(max_length=2000,
                             unique=False,
                             null=False,
                             blank=False)

    study_design = models.CharField(max_length=50, unique=False, blank=False)

    country = models.CharField(max_length=100, null=False, blank=False)
    region = models.CharField(max_length=100,
                              default=None,
                              null=True,
                              blank=False)
    urbanization = models.CharField(max_length=50,
                                    default=None,
                                    null=True,
                                    blank=False)
    cityvillage = models.CharField(max_length=50,
                                   default=None,
                                   null=True,
                                   blank=False)
    ethnicity = models.CharField(max_length=50,
                                 default=None,
                                 null=True,
                                 blank=False)
    elo = models.CharField(max_length=20, default=None, null=True, blank=False)

    diets = models.CharField(max_length=100,
                             default=None,
                             null=True,
                             blank=False)
    platform = models.CharField(max_length=100, null=False, blank=False)
    technology = models.CharField(max_length=100, null=False, blank=False)
    assay = models.CharField(max_length=100,
                             default=None,
                             null=True,
                             blank=False)
    target_amplicon = models.CharField(max_length=50,
                                       default=None,
                                       null=True,
                                       blank=False)
    bodysite = models.CharField(max_length=100, null=False, blank=False)
    participant_feature = models.CharField(max_length=1000,
                                           null=True,
                                           blank=True)
    sample_type = models.CharField(max_length=100, null=True, blank=True)

    disease = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    doid = models.CharField(max_length=100,
                            default=None,
                            null=True,
                            blank=False)
    sampid = models.CharField(max_length=100,
                              unique=False,
                              null=False,
                              blank=False)
    avspotlen = models.IntegerField(null=False,
                                    blank=False)  # Average spot length
    # TODO: How to reset to default when date is null??
    col_date = models.DateField(default=None, null=True, blank=False)
    lib_layout = models.CharField(max_length=20)
    coordinate = models.CharField(max_length=50,
                                  null=True,
                                  blank=False,
                                  default=None)


class Pubmed(models.Model):
    pubid = models.CharField(max_length=20,
                             unique=True,
                             null=False,
                             blank=False)
    # doi = models.CharField(max_length=100, unique=True, blank=False)
    title = models.CharField(max_length=1000,
                             unique=True,
                             null=False,
                             blank=False)

    class Meta:
        ordering = ["pubid", "title"]  # "doi",

    def __str__(self):
        full_res = f"""
        pubid:{self.pubid}
        title:{self.title}
        """
        return full_res


class StudyDesign(models.Model):
    """Docstring for StudyDesign."""

    study_design = models.CharField(max_length=50, unique=True, blank=False)

    def __str__(self):
        """TODO: to be defined."""
        return self.study_design


class BioProject(models.Model):
    repoid = models.CharField(max_length=100,
                              unique=True,
                              null=False,
                              blank=False)
    # l2study_design = models.ManyToManyField(StudyDesign)
    # TODO: Becareful about 0 value
    sample_size = models.IntegerField(default=0, null=False, blank=False)
    participants_summary = models.TextField(max_length=1000,
                                            null=True,
                                            blank=True)

    # TODO: Make it autoupdate field
    # TODO : Auto update using signal feature in Django
    # date_start = models.DateField(
    # default=date_default, null=False, blank=False)
    # date_end = models.DateField(default=date_default, null=False, blank=False)

    class meta:
        order = ["repoid"]

    def __str__(self):
        return f"""
        repoid:{self.repoid}
        """


# #
#     class Meta:
#         ordering = ["repoid"]
# # #
#
#     def __str__(self):
#         full_res = f"""
#         repoid:{self.repoid}
#         repo:{self.repo}
#         title:{self.title}
#         sample_size:{self.sample_size}
#         """
#         # TODO: Add value for many to many feature
#         return full_res
# #
#
#
class LocEthDiet(models.Model):
    country = models.CharField(max_length=100, null=False, blank=False)
    region = models.CharField(max_length=100,
                              default=None,
                              null=True,
                              blank=False)
    urbanization = models.CharField(max_length=50,
                                    default=None,
                                    null=True,
                                    blank=False)
    cityvillage = models.CharField(max_length=50,
                                   default=None,
                                   null=True,
                                   blank=False)
    ethnicity = models.CharField(max_length=50,
                                 default=None,
                                 null=True,
                                 blank=False)
    elo = models.CharField(max_length=20, default=None, null=True, blank=False)
    el_wiki = models.CharField(max_length=100,
                               default=None,
                               null=True,
                               blank=False)
    diets = models.CharField(max_length=100,
                             default=None,
                             null=True,
                             blank=False)

    class Meta:
        ordering = [
            "country",
            "region",
            "urbanization",
            "cityvillage",
            "ethnicity",
            "elo",
            "diets",
        ]

    def __str__(self):
        full_res = f"""
        country:{self.country}
        region:{self.region}
        urbanization:{self.urbanization}
        cityvillage:{self.cityvillage}
        ethnicity:{self.ethnicity}
        diet:{self.diets}
        """
        return full_res


#
#
# #
# #
#
#


class Platform(models.Model):
    platform = models.CharField(max_length=100, null=False, blank=False)
    technology = models.CharField(max_length=100, null=False, blank=False)
    assay = models.CharField(max_length=100,
                             default=None,
                             null=True,
                             blank=False)
    target_amplicon = models.CharField(max_length=50,
                                       default=None,
                                       null=True,
                                       blank=False)

    #

    class Meta:
        ordering = ["platform", "technology", "assay", "target_amplicon"]

    #

    def __str__(self):
        return f"""
        platform:{self.platform}
        technology:{self.technology}
        assay:{self.assay}
        target_amplicon:{self.target_amplicon}
        """


#
#


class BodySite(models.Model):
    bodysite = models.CharField(max_length=100, null=False, blank=False)

    # sampletype = models.CharField(max_length=100, null=False, black=False)

    class Meta:
        ordering = ["bodysite"]

    def __str__(self):
        full_res = f"""
        bodysite: {self.bodysite}
        """
        return full_res


class Disease(models.Model):
    """Docstring for Disease."""

    disease = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    doid = models.IntegerField(default=None, null=True, blank=False)

    class Meta:
        ordering = ["disease"]

    def __str__(self):
        full_res = f"""
        disease: {self.disease}:{self.doid}
        """
        return full_res


#
#


class Samples(models.Model):
    sampid = models.CharField(max_length=100,
                              unique=True,
                              null=False,
                              blank=False)
    avspotlen = models.IntegerField(null=True,
                                    blank=True)  # Average spot length
    participant_feature = models.CharField(max_length=1000,
                                           null=True,
                                           blank=True)
    sampletype = models.CharField(max_length=100, null=True, blank=True)
    bodysite = models.CharField(max_length=100, null=False, blank=False)
    # TODO: How to reset to default when date is null??
    col_date = models.DateField(default=None, null=True, blank=False)
    lib_layout = models.CharField(max_length=20)
    longitude = models.FloatField(null=True, blank=False, default=None)
    latitude = models.FloatField(null=True, blank=False, default=None)
    capital = models.BooleanField(default=False)
    l2pubmed = models.ManyToManyField(Pubmed)
    l2platform = models.ForeignKey(Platform,
                                   on_delete=models.SET_DEFAULT,
                                   default=None,
                                   null=True)
    l2bodysite = models.ForeignKey(BodySite,
                                   on_delete=models.SET_DEFAULT,
                                   default=None,
                                   null=True)
    l2disease = models.ManyToManyField(Disease)  # NOTE: One sample one disease
    # TODO: Check if sample has mixed disease
    # TODO: Add Participant summary
    is_mixed = models.BooleanField(default=False, null=False, blank=False)
    l2loc_diet = models.ForeignKey(LocEthDiet,
                                   on_delete=models.SET_DEFAULT,
                                   default=None,
                                   null=True)
    l2bioproject = models.ForeignKey(BioProject,
                                     on_delete=models.SET_DEFAULT,
                                     default=None,
                                     null=True)

    # TODO: Project should have this key, when current is deleted all the samples should deteleted

    class Meta:
        ordering = ["sampid"]

    # # #
    #

    def __str__(self):
        full_res = f"""
        sampid:{self.sampid}
        avspotlen:{self.avspotlen}
        """
        # col_date:{self.col_date}
        return full_res


class Tags(models.Model):
    tags = TaggableManager(help_text=None)
