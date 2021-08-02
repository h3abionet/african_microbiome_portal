#!/usr/bin/env python


"""MicroBiome Pages.

All the view Related to Microbiome will be will be written herobiome wbe will
be written here.
"""
import numpy as np
from numpy.lib.function_base import select
import pandas as pd

from .string2query import query2sqlquery

# For pagination
#  from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django_pandas.io import read_frame

from django.shortcuts import render
from django.db.models import Count, Q, F
from django.db.models.functions import Length
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.decorators.csrf import csrf_exempt

#  from django_tables2.config import RequestConfig
#  from .djmodel import get_model_repr
#  from .models import Movie, Person
from .forms import PostForm, Upload
from .models import (
    BioProject,
    BodySite,
    Disease,
    LocEthDiet,
    Platform,
    Pubmed,
    Samples,
    StudyDesign,
)
from .query_corrector import (
    amplicon_correct,
    assay_correct,
    bodysite_correct,
    loc_correct,
    platform_correct,
)

#  from django_tables2 import RequestConfig


#  from django.template import Context, loader
# https://docs.djangoproject.com/en/3.0/topics/http/file-uploads/
# def _savefile(infile):
# with open("Data/test.csv", "wb+") as fout:
# for chunk in infile.chunks():
# fout.write(chunk)


# def upload_file(request):
# if request.method == "POST":
# #  print("Kiran")
# formx = Upload(request.POST, request.FILES)
# #  print(request)
# if formx.is_valid():
# _ = _savefile(request.FILES["infile"])
# sep = formx.data["separator"]
# #  print("Anmol", sep)
# try:
# #  is_csv = len(open("Data/test.csv").readline().split(sep))
# #  if not is_csv:
# #      return render(request, 'warning2.html', {})
# #  df = pd.read_csv("Data/test.csv", sep=sep)
# df = pd.read_csv("Data/test.csv")
# print(df.head())

# # Must have colums
# must_have_colums = set(
# [
# "REPOSITORY ID",
# "STUDY TITLE",
# #  "REPOSITORY LINK",
# "SAMPLE NUMBER",
# "STUDY LINK",
# "ASSAY TYPE",
# "TECHNOLOGY",
# "COUNTRY",
# "DISEASE",
# "STUDY DESIGN",
# "BODY SITE",
# "PLATFORM",
# "PARTICIPANT FEATURES",
# #  "AVERAGE SPOTLENGTH",
# "LIBRARY LAYOUT",
# #  "LON LAT",
# "LAT LON",
# "SAMPLE TYPE",
# "COLLECTION DATE",
# "ETHNICITY",
# "URBANZATION",
# "REGION",
# #  "CITY",
# "CITYVILLAGE",
# "TARGET AMPLICON",
# "DIET",
# ]
# )
# column_not_found = must_have_colums - set(df.columns)
# if column_not_found:
# return render(
# request, "warning.html", {"columns": column_not_found}
# )
# #  print(column_not_found)
# df_dict = {}

# #  for col in must_have_colums:
# #      #  print(col)
# #      # Unknown
# #      col_val = Project.objects.order_by().values_list(
# #          col.replace(" ", "_").lower()).distinct()
# #      #  print(col_val)
# #      updated_list = []
# #      for val in set(df[col]):
# #          if (val,) in col_val:
# #              updated_list.append(str(val))
# #          else:
# #              updated_list.append(str(val)+"*")
# #      df_dict[col] = updated_list
# #  return render(request, 'overview.html', {'results': df_dict})
# except:
# return render(request, "warning2.html", {})

# else:
# formx = Upload()
# return render(request, "uploads.html", {"form": formx})


# Create your views here.


# def project_update(df):
# # Make everything in uppcase
# for _, row in df.drop_duplicates("REPOSITORY ID").iterrows():
# if not TestProject.objects.filter(repoid__exact=row["REPOSITORY ID"]):
# TestProject.objects.get_or_create(
# repoid=row["REPOSITORY ID"],
# repo=row["REPOSITORY LINK"],
# title=row["STUDY TITLE"],
# sample_size=None
# if pd.isna(row["SAMPLE NUMBER"])
# else row["SAMPLE NUMBER"],
# )


# def loc_eth_diest_update(df):
# for _, row in df.drop_duplicates(
# [
# "COUNTRY",
# "REGION",
# "URBANZATION",
# "CITYVILLAGE",
# "ETHNICITY",
# "DIET",
# "LAT LON",
# ]
# ).iterrows():
# print(row)

# # Split the coutry and coodindate
# LocEthDiet.objects.get_or_create(
# country=row["COUNTRY"],
# region=row["REGION"],
# urbanization=row["URBANZATION"],
# cityvillage=row["CITYVILLAGE"],
# ethnicity=row["ETHNICITY"],
# diets=row["DIET"],
# lon=float(row["LAT LON"].strip("*").split(",")[1]),
# lat=float(row["LAT LON"].split(",")[0]),
# )


# def platform_update(df):
# for _, row in df.drop_duplicates(["PLATFORM"]).iterrows():
# Platform.objects.get_or_create(platform=row["PLATFORM"])


# def assay_update(df):
# for _, row in df.drop_duplicates(["ASSAY TYPE"]).iterrows():
# Assay.objects.get_or_create(assay=row["ASSAY TYPE"])


# def amplicon_update(df):
# for _, row in df.drop_duplicates(["TARGET AMPLICON"]).iterrows():
# Amplicon.objects.get_or_create(amplicon=row["TARGET AMPLICON"])


# def bodysite_update(df):
# for _, row in df.drop_duplicates(["BODY SITE"]).iterrows():
# BodySite.objects.get_or_create(bodysite=row["BODY SITE"])


# def sample_update(df):
# for _, row in df.drop_duplicates("Run ID").iterrows():

# if not Samples.objects.filter(sampid__exact=row["Run ID"]):
# locdiet = loc_correct(
# row[
# [
# "COUNTRY",
# "REGION",
# "URBANZATION",
# "CITYVILLAGE",
# "ETHNICITY",
# "DIET",
# "LAT LON",
# ]
# ]
# )
# platform = platform_correct(row[["PLATFORM"]])
# assay = assay_correct(row[["ASSAY TYPE"]])
# amplicon = amplicon_correct(row[["TARGET AMPLICON"]])
# bodysite = bodysite_correct(row[["BODY SITE"]])
# #  platform = platform_correct(["PLATFORM"])
# print(row["Run ID"], "Acbnol kiran")
# print(platform["PLATFORM"], "Foolish Anmololol")
# samp = Samples.objects.create(
# sampid=row["Run ID"],
# avspotlen=None
# if pd.isna(row["AVERAGE SPOTLENGTH"])
# else row["AVERAGE SPOTLENGTH"],
# coldate=row["COLLECTION DATE"],
# locetdiet=LocEthDiet.objects.filter(
# country__exact=locdiet["COUNTRY"],
# region__exact=locdiet["REGION"],
# urbanization__exact=locdiet["URBANZATION"],
# cityvillage__exact=locdiet["CITYVILLAGE"],
# ethnicity__exact=locdiet["ETHNICITY"],
# diets__exact=locdiet["DIET"],
# lon__exact=float(row["LAT LON"].strip("*").split(",")[1]),
# lat__exact=float(row["LAT LON"].split(",")[0]),
# )[0],
# platform=Platform.objects.filter(
# platform__exact=platform["PLATFORM"]
# )[0],
# bodysite=BodySite.objects.filter(
# bodysite__exact=bodysite["BODY SITE"]
# )[0],
# assay=Assay.objects.filter(assay__exact=assay["ASSAY TYPE"])[
# 0
# ],
# amplicon=Amplicon.objects.filter(
# amplicon__exact=amplicon["TARGET AMPLICON"]
# )[0],
# project=TestProject.objects.filter(
# repoid=row["REPOSITORY ID"]
# )[0],
# )
# if pd.isna(row["DISEASE"]):
# dis = Disease.objects.filter(disease="nan", doid=None)
# samp.disease.add(*dis)
# elif pd.isna(row["DOID"]):
# diseases = row["DISEASE"].split(",")
# for di in diseases:
# dis = Disease.objects.filter(disease=di, doid=None)
# samp.disease.add(*dis)
# else:
# diseases = row["DISEASE"].split(",")
# doids = row["DOID"].split(",")
# if len(diseases) == len(doids):
# for di, do in zip(diseases, doids):
# tdo = do.split(":")
# if len(tdo) > 1:
# tdo = int(tdo[1])
# else:
# tdo = None
# dis = Disease.objects.filter(disease=di, doid=tdo)
# samp.disease.add(*dis)


# def disease_update(df):
# # Many to , many
# for _, row in df.drop_duplicates(["DISEASE", "DOID"]).iterrows():
# print(row, "Vwarsha")
# if pd.isna(row["DISEASE"]):
# Disease.objects.get_or_create(disease="nan", doid=None)
# elif pd.isna(row["DOID"]):
# diseases = row["DISEASE"].split(",")
# for di in diseases:
# Disease.objects.get_or_create(disease=di, doid=None)
# else:
# diseases = row["DISEASE"].split(",")
# doids = row["DOID"].split(",")
# if len(diseases) == len(doids):
# for di, do in zip(diseases, doids):
# tdo = do.split(":")
# if len(tdo) > 1:
# tdo = int(tdo[1])
# else:
# tdo = None
# Disease.objects.get_or_create(disease=di, doid=tdo)


# def update_counts():
# pass


# def pubmed_update(df):
# pass


# def test_update2():
# df = pd.read_csv("Data/test.csv")
# for col in df.columns:
# try:
# #  print(col)
# df[col] = df[col].apply(lambda x: x.strip().upper())
# df.loc[df[col] == "", col] = "NA"
# except:
# continue
# print(df.columns)
# table_order = [
# "TestProject",
# "Assay",
# "Amplicon",
# "LocEthDiet",
# "Platform",
# "Disease",
# "BodySite",
# "Samples",
# ]
# for tab in table_order:
# if tab == "TestProject":
# project_update(df)
# elif tab == "Samples":
# sample_update(df)
# elif tab == "LocEthDiet":
# loc_eth_diest_update(df)
# elif tab == "Platform":
# platform_update(df)
# elif tab == "Amplicon":
# amplicon_update(df)
# elif tab == "Assay":
# assay_update(df)
# elif tab == "Disease":
# disease_update(df)
# elif tab == "BodySite":
# bodysite_update(df)
# else:
# continue
def mergedict(args):
    """Returns merged dictionary."""
    output = {}
    for arg in args:
        output.update(arg)
    return output


def search_form(request):
    form = PostForm()

    # NOTE: BODY SITE
    body_site_project = BodySite.objects.all().annotate(
        num_samples=Count("samples__bioproject", distinct=True)
    )
    body_site_sample = BodySite.objects.all().annotate(num_samples=Count("samples"))
    body_site_pie_project = [
        {"name": plts.bodysite, "y": plts.num_samples}
        for plts in body_site_project
        if plts.bodysite != "nan"
    ]
    body_site_pie_sample = [
        {"name": plts.bodysite, "y": plts.num_samples}
        for plts in body_site_sample
        if plts.bodysite != "nan"
    ]

    # NOTE: ASSAY
    assay_project = (
        Platform.objects.values("assay")
        .annotate(num_samples=Count("samples__bioproject", distinct=True))
        .order_by("assay")
    )
    assay_sample = (
        Platform.objects.values("assay")
        .annotate(num_samples=Count("samples", distinct=True))
        .order_by("assay")
    )

    assay_pie_project = [
        {"name": plts["assay"], "y": plts["num_samples"]} for plts in assay_project
    ]

    assay_pie_sample = [
        {"name": plts["assay"], "y": plts["num_samples"]} for plts in assay_sample
    ]

    # NOTE: PLATFORM
    platforms_project = (
        Platform.objects.values("platform")
        .annotate(num_samples=Count("samples__bioproject", distinct=True))
        .order_by("platform")
    )
    platforms_sample = (
        Platform.objects.values("platform")
        .annotate(num_samples=Count("samples", distinct=True))
        .order_by("platform")
    )

    platform_pie_dict_project = [
        {"name": plts["platform"], "y": plts["num_samples"]}
        for plts in platforms_project
    ]

    platform_pie_dict_sample = [
        {"name": plts["platform"], "y": plts["num_samples"]}
        for plts in platforms_sample
    ]

    # NOTE: This code is for future reference, do not delete
    # Body Site
    #      bodysites = BodySite.objects.annotate(num_samples=Count("samples"))
    #      color = {'eye':"#90ED7D",
    #  'genital':"#434348",
    #  'gut':"#70A0CF",
    #  'lung':"#F7A35C",
    #  'milk':"#8085E9",
    #  'nasopharyngeal':"#F15C80",
    #  'oral':"#E4D354",
    #  'plasma':"#2B908F",
    #  'skin':"#F45B5B"}
    #      bodysite_pie_dict = [{'name': bs.bodysite,
    #                            'y': bs.num_samples,
    #                            } for bs in bodysites
    #                            #  'color':color[bs.bodysite]} for bs in bodysites
    #                           if not (bs.bodysite in ["Ebola virus",'nan', 'penil,vaginal'] or 'metagenom' in bs.bodysite)]

    # NOTE: DISEASES

    disease_project = Disease.objects.all().annotate(
        num_samples=Count("samples__bioproject", distinct=True)
    )
    disease_sample = Disease.objects.all().annotate(num_samples=Count("samples"))
    disease_pie_project = [
        {"name": plts.disease, "y": plts.num_samples} for plts in disease_project
    ]
    disease_pie_sample = [
        {"name": plts.disease, "y": plts.num_samples} for plts in disease_sample
    ]

    # NOTE: Geographical plotting on map
    geoloc_project = pd.DataFrame(
        Samples.objects.values("longitude", "latitude")
        .annotate(num_project=Count("bioproject", distinct=True))
        .order_by("longitude", "latitude")
    )

    geoloc_sample = pd.DataFrame(
        Samples.objects.values("longitude", "latitude")
        .order_by()
        .annotate(num_samples=Count("longitude"))
    )
    geoloc_country = pd.DataFrame(
        pd.DataFrame(
            Samples.objects.values(
                "longitude", "latitude", "loc_diet__country")
            .order_by("longitude", "latitude", "loc_diet__country")
            .distinct()
        )
    )
    geoloc = (
        geoloc_project.merge(geoloc_sample, on=[
                             "longitude", "latitude"], how="outer")
        .merge(geoloc_country, on=["longitude", "latitude"], how="outer")
        .rename(
            columns={
                "longitude": "lon",
                "latitude": "lat",
                "loc_diet__country": "country",
            }
        )
    )

    context = {
        "form": form,
        "body_site_pie_dict_project": body_site_pie_project,
        "body_site_pie_dict_sample": body_site_pie_sample,
        "assay_pie_dict_project": assay_pie_project,
        "assay_pie_dict_sample": assay_pie_sample,
        "disease_pie_dict_project": disease_pie_project,
        "disease_pie_dict_sample": disease_pie_sample,
        "platform_pie_dict_sample": platform_pie_dict_sample,
        "platform_pie_dict_project": platform_pie_dict_project,
        "records": geoloc,
    }
    # #  print(all_records.values())
    return render(request, "search.html", context)


#  return render(request, "search.html", {"form": form})


#  def results_download(request):
#      if request.method == "GET":
#          form = PostForm(request.GET)
#          print("Anmol", form)
#          if form.is_valid():
#              print("Kiran")
#          country = form.cleaned_data["country"]
#          platform = form.cleaned_data["platform"]
#          disease = form.cleaned_data["disease"]
#          study_design = form.cleaned_data["study_design"]
#          #  page = request.GET.get('page', 1)
#          res = Project.objects.all()
#          if country:
#              res = res.filter(country__icontains=country)
#          if platform:
#              res = res.filter(platform__icontains=country)
#          if disease:
#              res = res.filter(disease__icontains=country)
#          if study_design:
#              res = res.filter(study_design__icontains=country)
#          csv = pd.DataFrame(list(res.values()))
#          print(csv)
#          csv = csv.to_csv(index=False)
#          print(csv)
#          return render(request, "csv.html", {'csv': csv})
# https://stackoverflow.com/questions/16458166/how-to-disable-djangos-csrf-validation
@csrf_exempt
def results_sample(request):
    # Try https://github.com/jamespacileo/django-pure-pagination
    if request.method == "GET":
        tags = request.GET.get("tags", None)
        page = request.GET.get("page", 1)
        project = request.GET.get("project", None)
        qs = []
        extras = {}
        if project:
            qs.append(Q(project__repoid=project))
            extras["project"] = project
        query = qs.pop()
        for q in qs:
            query &= q

        print(project, tags)

        if tags:
            #             broken_tags = tags.split(",")
            #             qs = [
            #                 Q(sampid__icontains=tag)
            #                 | Q(avspotlen__icontains=tag)
            #                 | Q(locetdiet__country__icontains=tag)
            #                 | Q(locetdiet__region__icontains=tag)
            #                 | Q(locetdiet__urbanization__icontains=tag)
            #                 | Q(locetdiet__cityvillage__icontains=tag)
            #                 | Q(locetdiet__ethnicity__icontains=tag)
            #                 | Q(locetdiet__country__icontains=tag)
            #                 | Q(platform__platform__icontains=tag)
            #                 | Q(amplicon__amplicon__icontains=tag)
            #                 | Q(assay__assay__icontains=tag)
            #                 | Q(disease__disease__icontains=tag)
            #                 for tag in broken_tags
            #             ]
            #             # print(tags, broken_tags)
            #             query2 = qs.pop()
            #             for q in qs:
            #                 query2 |= q
            #             query &= query2
            #
            #         print(query, "Anmol")
            query = query2sqlquery(tags)
            print(query, "anmol kiarn")

        res = Samples.objects.filter(query).values(
            "sampid",
            "locetdiet__country",
            "platform__platform",
            "amplicon__amplicon",
            "assay__assay",
            "disease__disease",
            "locetdiet__lon",
            "locetdiet__lat",
        )
        df = read_frame(res).replace("nan", "")

        print(df)
        paginator = Paginator(
            df.to_dict(orient="records"), 10
        )  # 10 information per page

        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)

        # print(items, "anmol",df.to_dict(orient="records"),page)

        index = items.number - 1
        max_index = len(paginator.page_range)
        start_index = index - 5 if index >= 5 else 0
        end_index = index + 5 if index <= max_index - 5 else max_index
        page_range = paginator.page_range[start_index:end_index]
        # Platforms
        platform = read_frame(
            res.annotate(num=Count("platform__platform")
                         ).order_by("platform__platform")
        )
        platform = (
            platform.groupby("platform__platform")[
                "num"].apply(np.sum).reset_index()
        )

        platform_pie_dict = [
            {"name": plts["platform__platform"], "y": plts["num"]}
            for _, plts in platform.iterrows()
            if plts["platform__platform"] != "nan"
        ]

        # ASSAY
        assay = read_frame(
            res.annotate(num=Count("assay__assay")).order_by("assay__assay")
        )
        assay = assay.groupby("assay__assay")[
            "num"].apply(np.sum).reset_index()
        print(assay)

        assay_pie_dict = [
            {"name": plts["assay__assay"], "y": plts["num"]}
            for _, plts in assay.iterrows()
            if plts["assay__assay"] != "nan"
        ]

        # DISEASES
        disease = read_frame(
            res.annotate(num=Count("disease__disease")
                         ).order_by("disease__disease")
        )
        disease = disease.groupby("disease__disease")[
            "num"].apply(np.sum).reset_index()

        disease_pie_dict = [
            {"name": plts["disease__disease"], "y": plts["num"]}
            for _, plts in disease.iterrows()
            if plts["disease__disease"] != "nan"
        ]
        # # GEO LOCATION
        try:
            geoloc = pd.DataFrame(
                res.values(
                    "locetdiet__lon",
                    "locetdiet__lat",
                    "locetdiet__country",
                    "project",
                )
                #  LocEthDiet.objects.values(
                #  "lon", "lat","country").annotate(num_samples=Count("samples__project", distinct=True))
            )
            # TODO: Fix country issue with multiple coordinates
            geoloc = geoloc[
                ~(pd.isna(geoloc.locetdiet__lon) | pd.isna(geoloc.locetdiet__lat))
            ].drop_duplicates(["locetdiet__country", "project"])
            geoloc_country = geoloc.drop_duplicates("locetdiet__country")
            for _, row in geoloc_country.iterrows():
                geoloc.loc[
                    geoloc["locetdiet__country"] == row["locetdiet__country"],
                    "locetdiet__lon",
                ] = row["locetdiet__lon"]
                geoloc.loc[
                    geoloc["locetdiet__country"] == row["locetdiet__country"],
                    "locetdiet__lat",
                ] = row["locetdiet__lat"]
            geoloc = (
                geoloc.groupby(
                    ["locetdiet__lon", "locetdiet__lat", "locetdiet__country"]
                )
                .size()
                .reset_index()
                .rename(
                    columns={
                        0: "num_samples",
                        "locetdiet__lon": "lon",
                        "locetdiet__lat": "lat",
                        "locetdiet__country": "country",
                    }
                )
            )

            #  geoloc = pd.DataFrame(res.values("locetdiet__lon", "locetdiet__lat", "locetdiet__country","project")
            #      #  LocEthDiet.objects.values(
            #      #  "lon", "lat","country").annotate(num_samples=Count("samples__project", distinct=True))
            #                        )
            #  # TODO: Fix country issue with multiple coordinates
            #  geoloc = geoloc[~(pd.isna(geoloc.locetdiet__lon) | pd.isna(geoloc.locetdiet__lat))].drop_duplicates(["locetdiet__country","project"])
            #  geoloc_country = geoloc.drop_duplicates()
            #  for _, row in geoloc_country.iterrows():
            #      geoloc.loc[geoloc["locetdiet__country"] == row["locetdiet__country"], "locetdiet__lon" ] = row["locetdiet__lon"]
            #      geoloc.loc[geoloc["locetdiet__country"] == row["locetdiet__country"], "locetdiet__lat" ] = row["locetdiet__lat"]
            #  geoloc = geoloc.groupby(["locetdiet__lon", "locetdiet__lat","clocetdiet__ountry"])["num_samples"].apply(sum).reset_index()
            #  print(geoloc, "Anmol")
            #
            #
            #
            #  geoloc = pd.DataFrame(res.values("locetdiet__lon", "locetdiet__lat"))
            #  geoloc = geoloc[~(pd.isna(geoloc.locetdiet__lat) | pd.isna(geoloc.locetdiet__lon))]
            #  geoloc = geoloc.groupby(["locetdiet__lon", "locetdiet__lat"]).size(
            #  ).reset_index().rename(columns={"locetdiet__lon":"lon", "locetdiet__lat":"lat", 0:"num_samples"})
        except AttributeError:
            geoloc = pd.DataFrame()
        no_data = [{"name": "No Data", "y": 0}]
        print(assay_pie_dict)
        return render(
            request,
            "sample_results.html",
            {
                "results": items,  # "results_samples.html"
                "tags": tags,
                "extras": extras,
                "platform_pie_dict_sample": platform_pie_dict
                if platform_pie_dict
                else no_data,
                "assay_pie_dict_sample": (
                    assay_pie_dict if assay_pie_dict else no_data
                ),
                "disease_pie_dict_sample": disease_pie_dict
                if disease_pie_dict
                else no_data,
                "records": geoloc,
                # Pagination
                "page_range": page_range,
                "items": items
                # 'query': query[: -1]
            },
        )


def results(request):
    # Try https://github.com/jamespacileo/django-pure-pagination
    if request.method == "POST":
        search_text = request.POST["tags"]
        tags = request.POST["oldsearch"]
        page = 1
        qt = "post"

    if request.method == "GET":
        tags = request.GET.get("tags", None)
        page = request.GET.get("page", 1)
        search_text = None
        qt = "get"

    res = None
    if not tags:
        # res = TestProject.objects.all()
        res = Pubmed.objects.annotate(
            bioproject=F("samples__bioproject__repoid"),
            sampleid=F("samples__sampid"),
            country=F("samples__loc_diet__country"),
            platform=F("samples__platform__platform"),
            amplicon=F("samples__platform__target_amplicon"),
            assay=F("samples__platform__assay"),
            disease=F("samples__disease__disease"),
            lon=F("samples__longitude"),
            lat=F("samples__latitude"),
        ).values(
            "title",
            "pubid",
            "bioproject",
            "sampleid",
            "country",
            "platform",
            "amplicon",
            "assay",
            "disease",
            "lon",
            "lat",
        )
        # print(res)
    else:
        # broken_tags = set(tags.split(","))
        # qs = [
        #     Q(sampid__icontains=tag)
        #     | Q(avspotlen__icontains=tag)
        #     | Q(project__title__icontains=tag)
        #     | Q(locetdiet__country__icontains=tag)
        #     | Q(locetdiet__region__icontains=tag)
        #     | Q(locetdiet__urbanization__icontains=tag)
        #     | Q(locetdiet__cityvillage__icontains=tag)
        #     | Q(locetdiet__ethnicity__icontains=tag)
        #     | Q(platform__platform__icontains=tag)
        #     | Q(amplicon__amplicon__icontains=tag)
        #     | Q(assay__assay__icontains=tag)  # |
        #     #   Q(disease__disease__icontains=tag)
        #     for tag in broken_tags
        # ]
        # query = qs.pop()
        # for q in qs:
        #     query |= q
        print(tags)
        query = query2sqlquery(tags)

        # res = Samples.objects.filter(query).values(
        # "project__repoid",
        # "project__title",
        # "locetdiet__country",
        # "platform__platform",
        # "amplicon__amplicon",
        # "assay__assay",
        # "disease__disease",
        # "locetdiet__lon",
        # "locetdiet__lat",
        # "locetdiet__cityvillage",
        # "locetdiet__urbanization",
        # "locetdiet__diets",
        # "locetdiet__ethnicity",
        # "locetdiet__region",
        # )  # .annotate(sample_size=Count("project__repoid")).order_by('project__repoid')
    # # print(read_frame(res))
    # if search_text:
    # broken_tags = set(search_text.split(","))
    # qs = [
    # Q(sampid__icontains=tag)
    # | Q(avspotlen__icontains=tag)
    # | Q(project__title__icontains=tag)
    # | Q(locetdiet__country__icontains=tag)
    # | Q(locetdiet__region__icontains=tag)
    # | Q(locetdiet__urbanization__icontains=tag)
    # | Q(locetdiet__cityvillage__icontains=tag)
    # | Q(locetdiet__ethnicity__icontains=tag)
    # | Q(platform__platform__icontains=tag)
    # | Q(amplicon__amplicon__icontains=tag)
    # | Q(assay__assay__icontains=tag)  # |
    # #   Q(disease__disease__icontains=tag)
    # for tag in broken_tags
    # ]
    # query = qs.pop()
    # for q in qs:
    # query |= q
    # res = res.filter(query)

    try:
        project_summary = read_frame(
            res.values(
                "pubid",
                "title",
                "bioproject",
                "country",
                "disease",
                "platform",
                "assay",
                "amplicon",
                "lon",
                "lat",
            )
            # .annotate(samp_size=Count("sampleid"))
            # .order_by("pubid", "title", "bioproject", "country", "disease", "platform", "assay", "amplicon"),
            # fieldnames=["pubid", "title",
            # "bioproject", "country", "disease", "platform", "assay", "amplicon", "samp_size"],
        )
        geo = (
            project_summary.groupby(["lon", "lat"])
            .size()
            .reset_index()
            .rename(columns={0: "num_samples"})
        )  # TODO: Might need to drop dumplcates
        geo_country = project_summary[[
            "lon", "lat", "country"]].drop_duplicates()
        geo_projects = (
            project_summary[["lon", "lat", "bioproject"]]
            .drop_duplicates()
            .groupby(["lon", "lat"])
            .size()
            .reset_index()
            .rename(columns={0: "num_project"})
        )
        geo = geo.merge(geo_country, on=["lon", "lat"], how="outer").merge(
            geo_projects, on=["lon", "lat"], how="outer"
        )
        print(geo)

        project_summary = project_summary.melt(id_vars=["pubid", "title"])

        project_summary = project_summary[~pd.isna(project_summary["value"])]
        # print(project_summary)
        # NOTE: Platform pie
        platform_pie_dict_sample = (
            project_summary[project_summary["variable"] == "platform"]
            .groupby("value")
            .size()
            .reset_index()
            .rename(columns={"value": "name", 0: "y"})
            .to_json(orient="records")
        )

        disease_pie_dict_sample = (
            project_summary[project_summary["variable"] == "disease"]
            .groupby("value")
            .size()
            .reset_index()
            .rename(columns={"value": "name", 0: "y"})
            .to_json(orient="records")
        )

        assay_pie_dict_sample = (
            project_summary[project_summary["variable"] == "assay"]
            .groupby("value")
            .size()
            .reset_index()
            .rename(columns={"value": "name", 0: "y"})
            .to_json(orient="records")
        )

        # print(platform_pie_dict_sample)

        project_summary = (
            project_summary.groupby(["pubid", "title", "variable", "value"])
            .size()
            .reset_index()
        )
        # project_summary["value"] = project_summary["value"] + \
        # "("+project_summary[0].astype(str)+")"
        project_summary["value"] = project_summary[["value", 0]].apply(
            lambda x: {x["value"]: x[0]}, axis=1
        )
        # TODO: Use dictionary
        del project_summary[0]
        # project_summary = project_summary.groupby(["pubid", "title", "variable"])[
        # "value"].apply(lambda x: ",".join(x.values)).reset_index()

        project_summary = (
            project_summary.groupby(["pubid", "title", "variable"])["value"]
            .apply(list)
            .reset_index()
        )
        project_summary["value"] = project_summary["value"].apply(mergedict)
        # print(project_summary)
        project_summary = project_summary.pivot(
            index=["pubid", "title"], columns="variable", values="value"
        ).reset_index()

        # print(project_summary[["pubid", "title", "bioproject"]])
    except:
        project_summary = pd.DataFrame()

    paginator = Paginator(
        project_summary.to_dict(orient="records"), 10
    )  # 10 information per page

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    # print(items, "anmol",df.to_dict(orient="records"),page)

    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range = paginator.page_range[start_index:end_index]

    # print("Anmol Kiran", df)
    print(qt, items)
    if qt == "get":
        return render(
            request,
            "results.html",
            {
                "results": items,
                "tags": tags,
                "qt": qt,
                "platform_pie_dict_sample": platform_pie_dict_sample,
                "assay_pie_dict_sample": assay_pie_dict_sample,
                "disease_pie_dict_sample": disease_pie_dict_sample,
                "records": geo,
                # Pagination
                "page_range": page_range,
                "items": items
                # 'query': query[: -1]
            },
        )
    else:
        # print(disease_pie_dict, "this is test")
        # return render_to_response("results_refine.html", {'results': items,
        return render(
            None,
            "results_refine.html",
            {
                "results": items,
                # 'tags': tags,
                # "qt":qt,
                "platform_pie_dict": platform_pie_dict,
                "assay_pie_dict": assay_pie_dict,
                "disease_pie_dict": disease_pie_dict,
                "records": geoloc,
                # Pagination
                "page_range": page_range,
                "items": items
                # 'query': query[: -1]
            },
        )
    # else:
    #     response = redirect('/search/')
    #     return response


#  def results(request):
#      # Try https://github.com/jamespacileo/django-pure-pagination
#      if request.method == "GET":
#          form = PostForm(request.GET)
#          #  print(form.cleaned_data)
#          #  if form.is_valid():
#          #      print("Kiran", form.cleaned_data)
#          #  print(form.data['country'])
#          try:
#              country = form.data["country"]
#          except KeyError:
#              country = None
#          try:
#              tags = form.data["tags"]
#              print(tags.split(","))
#          except KeyError:
#              tags = None
#
#
#
#          try:
#              platform = form.data["platform"]
#          except KeyError:
#              platform = None
#          try:
#              disease = form.data["disease"]
#          except KeyError:
#              disease = None
#          try:
#              study_design = form.data["study_design"]
#          except KeyError:
#              study_design = None
#          #  page = request.GET.get('page', 1)
#          res = Project.objects.all()
#          if country:
#              res = res.filter(country__icontains=country)
#          if platform:
#              res = res.filter(platform__icontains=platform)
#          if disease:
#              res = res.filter(disease__icontains=disease)
#          if study_design:
#              res = res.filter(study_design__icontains=study_design)
#
#
#  #  posts = serverlist.objects.filter(
#  #       Q(Project__icontains=query)|Q(ServerName__icontains=query)
#  #  )
#  #  from django.db.models import Q
#  #  #get the current_user
#  #  current_user = request.user
#  #  keywords=  ['funny', 'old', 'black_humor']
#  #  qs = [Q(title__icontains=keyword)|Q(author__icontains=keyword)|Q(tags__icontains=keyword) for keyword in keywords]
#  #
#  #  query = qs.pop() #get the first element
#  #
#  #  for q in qs:
#  #      query |= q
#  #  filtered_user_meme = Meme.objects.filter(query, user=current_user)
#  #
#          res_count = len(res)
#          query = ""
#          for k, v in form.data.items():
#              query += "%s=%s&" % (k, v)
#          return render(request, "results.html", {'results': res, 'res_count': res_count,  'query': query[:-1]})
#      else:
#          form = PostForm()
#
#          all_records=Project.objects.all()
#          df = read_frame(all_records)
#          df = df.loc[~(pd.isnull(df.lat) | pd.isnull(df.lon)),
#                  ['lon', 'lat', 'sample_type', 'disease','platform',
#                      'country','sample_count']]
#          site_pie_dict = [{'name': item['body_site'],
#                              'y': item['type_count']} for item in \
#                                      all_records.values('body_site')\
#                                      .annotate(type_count=Count('body_site')) ]
#          #  print(site_pie_dict)
#
#          platform_pie_dict = [{'name': item['platform'], 'y': item['type_count'] } for item in all_records.values('platform').annotate(type_count=Count('sample_type')) ]
#
#          assay_type=pd.DataFrame(list(all_records.values('assay_type').annotate(type_count=Count('sample_type'))))
#          xdata_assay=list(assay_type['assay_type'])
#          ydata_assay=list(assay_type['type_count'])
#
#          disease=pd.DataFrame(list(all_records.values('disease').annotate(type_count=Count('disease'))))
#          xdata_disease=list(disease['disease'])
#          ydata_disease=list(disease['type_count'])
#          print("anmol")
#
#          context={#'form':form,
#                  'xdata_assay': xdata_assay,
#                  'ydata_assay': ydata_assay,
#                  'xdata_disease': xdata_disease,
#                  'ydata_disease': ydata_disease,
#                  'platform_pie_dict': platform_pie_dict,
#                  'site_pie_dict': site_pie_dict,
#                  'records': df};
#          #  print(all_records.values())
#          return render(request, "search.html", context=context)
#
#          #  return render(request, 'dashboard.html', context=context)

#  def summary(request):
#      all_records = Project.objects.all()
#      df = read_frame(all_records)
#      df = df.loc[~(pd.isnull(df.lat) | pd.isnull(df.lon)),
#                  ['lon', 'lat', 'sample_type', 'disease', 'platform',
#                   'country', 'sample_count']]
#      site_pie_dict = [{'name': item['body_site'],
#                        'y': item['type_count']} for item in
#                       all_records.values('body_site')
#                       .annotate(type_count=Count('body_site'))]
#      #  print(site_pie_dict)
#
#      platform_pie_dict = [{'name': item['platform'], 'y': item['type_count']}
#                           for item in all_records.values('platform').annotate(type_count=Count('sample_type'))]
#
#      assay_type = pd.DataFrame(list(all_records.values(
#          'assay_type').annotate(type_count=Count('sample_type'))))
#      xdata_assay = list(assay_type['assay_type'])
#      ydata_assay = list(assay_type['type_count'])
#
#      disease = pd.DataFrame(list(all_records.values(
#          'disease').annotate(type_count=Count('disease'))))
#      xdata_disease = list(disease['disease'])
#      ydata_disease = list(disease['type_count'])
#
#      context = {'xdata_assay': xdata_assay,
#                 'ydata_assay': ydata_assay,
#                 'xdata_disease': xdata_disease,
#                 'ydata_disease': ydata_disease,
#                 'platform_pie_dict': platform_pie_dict,
#                 'site_pie_dict': site_pie_dict,
#                 'records': df}
#      #  print(all_records.values())
#
#      return render(request, 'dashboard.html', context=context)


#  def summary(request):
#      """The Database Summary Page.
#      """
#      df = "/home/devil/Documents/Tools/Database/MicroBiome/test.csv"
#      all_records = pd.read_csv(
#          df,
#          usecols=["LON", "LAT", "SAMPLE_TYPE", "DISEASE", "PLATFORM", "COUNTRY", "SAMPLE_COUNT"])
#      all_records = all_records[~pd.isnull(all_records.LON)]
#
#      print(all_records.head().T.to_dict().values())
#      data = all_records.head().to_csv()
#      #  all_records = Project.objects.all()
#      #  return render(request, 'index.html', {'records': all_records,
#      return render(request, 'pivottablejs.html', {'records': all_records,
#                                            'data': data})
