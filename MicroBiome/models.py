from django.db import models
from datetime import date
from taggit.managers import TaggableManager

# https://stackoverflow.com/questions/2459979/how-to-import-csv-data-into-django-models

# https://stackoverflow.com/questions/21512647/how-to-count-the-amount-of-objects-in-a-django-joined-table

date_default = date(1, 1, 1)


class Pubmed(models.Model):
    pubid = models.IntegerField(
        max_length=20, unique=True, null=False, blank=False)
    # doi = models.CharField(max_length=100, unique=True, blank=False)
    title = models.CharField(
        max_length=1000, unique=True, null=False, blank=False)

    class Meta:
        ordering = ["pubid", "title"]  # "doi",

    def __str__(self):
        full_res = f"""
        pubid:{self.pubid}
        title:{self.title}
        """
        return full_res


class StudyDesign(models.Model):

    """Docstring for StudyDesign. """
    study_design = models.CharField(max_length=50, unique=True, blank=False)

    def __str__(self):
        """TODO: to be defined. """
        return self.study_design


class BioProject(models.Model):
    repoid = models.CharField(
        max_length=100, unique=True, null=False, blank=False)
    study_design = models.ManyToManyField(StudyDesign)
    # TODO: Becareful about 0 value
    sample_size = models.IntegerField(default=0, null=False, blank=False)
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
    region = models.CharField(
        max_length=100, default=None, null=True, blank=False)
    urbanization = models.CharField(
        max_length=50, default=None, null=True, blank=False)
    cityvillage = models.CharField(
        max_length=50, default=None, null=True, blank=False)
    ethnicity = models.CharField(
        max_length=50, default=None, null=True, blank=False)
    elo = models.CharField(max_length=20, default=None,
                           null=True, blank=False)
    # ethno_ling_wiki = models.CharField(max_length=100)
    diets = models.CharField(
        max_length=100, default=None, null=True, blank=False)

    class Meta:
        ordering = ["country", "region", "urbanization",
                    "cityvillage", "ethnicity", "elo", "diets"]

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
    assay = models.CharField(
        max_length=100, default=None, null=True, blank=False)
    target_amplicon = models.CharField(
        max_length=50, default=None, null=True, blank=False)
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

    class Meta:
        ordering = ["bodysite"]

    def __str__(self):
        full_res = f"""
        bodysite: {self.bodysite}
        """
        return full_res


class Disease(models.Model):
    """Docstring for Disease."""
    disease = models.CharField(max_length=100, null=False, blank=False,)
    doid = models.IntegerField(
        max_length=20, default=None, null=True, blank=False)

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
    sampid = models.CharField(
        max_length=100, unique=True, null=False, blank=False)
    avspotlen = models.IntegerField(max_length=5,
                                    null=False, blank=False
                                    )  # Average spot length
    # TODO: How to reset to default when date is null??
    # col_date = models.DateField(default=date_default, null=True, blank=False)
    lib_layout = models.CharField(max_length=20)
    longitude = models.FloatField(null=True, blank=False, default=None)
    latitude = models.FloatField(null=True, blank=False, default=None)
    capital = models.BooleanField(default=False)
    pubmed = models.ManyToManyField(Pubmed)
    platform = models.ForeignKey(
        Platform, on_delete=models.SET_DEFAULT, default=None, null=True)
    bodysite = models.ForeignKey(
        BodySite, on_delete=models.SET_DEFAULT, default=None, null=True
    )
    disease = models.ManyToManyField(Disease)  # NOTE: One sample one disease
    # TODO: Check if sample has mixed disease
    is_mixed = models.BooleanField(default=False, null=False, blank=False)
    loc_diet = models.ForeignKey(
        LocEthDiet, on_delete=models.SET_DEFAULT, default=None, null=True)
    bioproject = models.ForeignKey(
        BioProject, on_delete=models.SET_DEFAULT, default=None, null=True)
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
