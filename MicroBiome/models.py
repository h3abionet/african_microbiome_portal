from django.db import models
from taggit.managers import TaggableManager

# https://stackoverflow.com/questions/2459979/how-to-import-csv-data-into-django-models

# https://stackoverflow.com/questions/21512647/how-to-count-the-amount-of-objects-in-a-django-joined-table


class TestProject(models.Model):
    repoid = models.CharField(max_length=100)
    repo = models.CharField(max_length=20, default="ncbi")
    title = models.CharField(max_length=500, default="No Title")
    sample_size = models.IntegerField(default=0)

    class Meta:
        ordering = ["repoid"]

    def __str__(self):
        full_res = f"""
        repoid:{self.repoid}
        repo:{self.repo}
        title:{self.title}
        sample_size:{self.sample_size}
        """
        return full_res


class Pubmed(models.Model):
    pubid = models.IntegerField(default=None)
    title = models.CharField(max_length=500, default="No Title")

    class Meta:
        ordering = ["pubid"]

    def __str__(self):
        full_res = f"""
        pubid:{self.pubid}
        title:{self.title}
        """


class LocEthDiet(models.Model):
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    urbanization = models.CharField(max_length=100)
    cityvillage = models.CharField(max_length=100)
    ethnicity = models.CharField(max_length=100)
    diets = models.CharField(max_length=100)
    lon = models.FloatField(null=True)
    lat = models.FloatField(null=True)

    class Meta:
        ordering = ["country"]

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


class Platform(models.Model):
    platform = models.CharField(max_length=100, default=None, null=True)

    class Meta:
        ordering = ["platform"]

    def __str__(self):
        return self.platform


class BodySite(models.Model):
    bodysite = models.CharField(max_length=400, default=None, null=True)

    class Meta:
        ordering = ["bodysite"]

    def __str__(self):
        return self.bodysite


class Disease(models.Model):
    disease = models.CharField(max_length=100)
    doid = models.IntegerField(default=None, null=True)

    class Meta:
        ordering = ["disease"]

    def __str__(self):
        full_res = f"{self.disease}:{self.doid}"
        return full_res


class Amplicon(models.Model):
    amplicon = models.CharField(max_length=50)

    class Meta:
        ordering = ["amplicon"]

    def __str__(self):
        return self.amplicon


class Assay(models.Model):
    assay = models.CharField(max_length=100)

    class Meta:
        ordering = ["assay"]

    def __str__(self):
        return self.assay


class Samples(models.Model):
    sampid = models.CharField(max_length=100)
    avspotlen = models.IntegerField(default=None, null=True) # Average spot length
    coldate = models.CharField(default=None, null=True, max_length=100)
    project = models.ForeignKey(
        TestProject, on_delete=models.CASCADE, default=None)
    disease = models.ManyToManyField(Disease)
    locetdiet = models.ForeignKey(
        LocEthDiet, on_delete=models.CASCADE, default=None)
    platform = models.ForeignKey(
        Platform, on_delete=models.CASCADE, default=None)
    amplicon = models.ForeignKey(
        Amplicon, on_delete=models.CASCADE, default=None)
    assay = models.ForeignKey(
        Assay, on_delete=models.CASCADE, default=None)
    bodysite = models.ForeignKey(
        BodySite, on_delete=models.CASCADE, default=None)

    class Meta:
        ordering = ["sampid"]

    def __str__(self):
        full_res = f"""
        sampid:{self.sampid}
        avspotlen:{self.avspotlen}
        coldate:{self.coldate}
        """
        return full_res


class Project(models.Model):
    repository_id = models.CharField(max_length=20)  # max length was 11
    study_title = models.CharField(max_length=410)  # max length was 308
    study_link = models.CharField(max_length=150)  # max length was 108
    assay_type = models.CharField(max_length=20)  # max length was 9
    technology = models.CharField(max_length=20)  # max length was 11
    country = models.CharField(max_length=60)  # max length was 41
    disease = models.CharField(max_length=100)  # max length was 75
    study_design = models.CharField(max_length=80)  # max length was 55
    body_site = models.CharField(max_length=50)  # max length was 31
    platform = models.CharField(max_length=40)  # max length was 28
    participant_features = models.CharField(
        max_length=280)  # max length was 212
    library_layout = models.CharField(max_length=10)  # max length was 7
    lon_lat = models.CharField(max_length=50)  # max length was 32
    sample_type = models.CharField(max_length=30)  # max length was 22
    collection_date = models.CharField(max_length=30)  # max length was 21
    ethnicity = models.CharField(max_length=110)  # max length was 84
    urbanzation = models.CharField(max_length=20)  # max length was 13
    region = models.CharField(max_length=150)  # max length was 108
    city = models.CharField(max_length=60)  # max length was 44
    target_amplicon = models.CharField(max_length=50)  # max length was 31
    diet = models.CharField(max_length=180)  # max length was 136
    # min: 1, max: 894, mean: 6.519581056466302
    sample_number = models.PositiveSmallIntegerField()
    tags = TaggableManager(help_text=None)

    def __str__(self):
        return self.study_title
