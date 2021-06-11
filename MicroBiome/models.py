from django.db import models
from taggit.managers import TaggableManager

# https://stackoverflow.com/questions/2459979/how-to-import-csv-data-into-django-models

# https://stackoverflow.com/questions/21512647/how-to-count-the-amount-of-objects-in-a-django-joined-table


# class TestProject(models.Model):
#     repoid = models.CharField(max_length=100, unique=True, blank=False)
#     repo = models.CharField(max_length=20, default="ncbi")
#     title = models.CharField(max_length=500, default="No Title")
#     sample_size = models.IntegerField(default=0)
#     # TODO: Make it autoupdate field
#     date_rage = models.CharField(max_length=100)
#
#     class Meta:
#         ordering = ["repoid"]
#
#     def __str__(self):
#         full_res = f"""
#         repoid:{self.repoid}
#         repo:{self.repo}
#         title:{self.title}
#         sample_size:{self.sample_size}
#         """
#         return full_res
#


class Pubmed(models.Model):
    pubid = models.CharField(max_length=20, unique=True, blank=False)
    # doi = models.CharField(max_length=100, unique=True, blank=False)
    title = models.CharField(max_length=1000, unique=True, blank=False)

    class Meta:
        ordering = ["pubid", "title"]  # "doi",

    def __str__(self):
        full_res = f"""
        pubid:{self.pubid}
        title:{self.title}
        """
        return full_res


class LocEthDiet(models.Model):
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    urbanization = models.CharField(max_length=100)
    cityvillage = models.CharField(max_length=100)
    ethnicity = models.CharField(max_length=100)
    elo = models.CharField(max_length=100)
    # ethno_ling_wiki = models.CharField(max_length=100)
    diets = models.CharField(max_length=100)
    lon = models.CharField(max_length=50, null=True)
    lat = models.CharField(max_length=50, null=True)
    # Incase position is pointed to capital city
    capital = models.BooleanField(default=False)

    class Meta:
        ordering = ["country", "region", "lon", "lat"]

    def __str__(self):
        full_res = f"""
        country:{self.country}
        region:{self.region}
        urbanization:{self.urbanization}
        cityvillage:{self.cityvillage}
        ethnicity:{self.ethnicity}
        diet:{self.diets}
        coordinate:{self.lon},{self.lat}
        """
        return full_res


#
#


class Platform(models.Model):
    platform = models.CharField(max_length=100, default=None, null=True)
    technology = models.CharField(max_length=100)
    assay = models.CharField(max_length=100)

    class Meta:
        ordering = ["platform", "technology", "assay"]

    def __str__(self):
        return f"""
        platform:{self.platform}
        technology:{self.technology}
        assay:{self.assay}
        """


#
#


class BodySite(models.Model):
    bodysite = models.CharField(max_length=100, default=None, null=True)

    class Meta:
        ordering = ["bodysite"]

    # #

    def __str__(self):
        full_res = f"""
        bodysite: {self.bodysite}
        """
        return full_res


#


class Disease(models.Model):

    """Docstring for Disease."""

    disease = models.CharField(max_length=100, blank=True, default=None)
    doid = models.CharField(
        max_length=100, default=None, null=True, blank=True)

    class Meta:
        ordering = ["disease"]

    def __str__(self):
        full_res = f"""
        disease: {self.disease}:{self.doid}
        """
        return full_res


#
#
# class Samples(models.Model):
#     sampid = models.CharField(max_length=100)
#     avspotlen = models.IntegerField(
#         default=None, null=True
#     )  # Average spot length
#     coldate = models.CharField(default=None, null=True, max_length=100)
#     project = models.ForeignKey(
#         TestProject, on_delete=models.CASCADE, default=None
#     )
#     disease = models.ManyToManyField(Disease)  # NOTE: One sample one disease
#     locetdiet = models.ForeignKey(
#         LocEthDiet, on_delete=models.CASCADE, default=None
#     )
#     platform = models.ForeignKey(
#         Platform, on_delete=models.CASCADE, default=None
#     )
#     bodysite = models.ForeignKey(
#         BodySite, on_delete=models.CASCADE, default=None
#     )
#
#     class Meta:
#         ordering = ["sampid"]
#
#     def __str__(self):
#         full_res = f"""
#         sampid:{self.sampid}
#         avspotlen:{self.avspotlen}
#         coldate:{self.coldate}
#         """
#         return full_res
