#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 17.08.2021
# Last Modified Date: 17.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 17.08.2021
# Last Modified Date: 17.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 17.08.2021
# Last Modified Date: 17.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 17.08.2021
# Last Modified Date: 17.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 17.08.2021
# Last Modified Date: 17.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 17.08.2021
# Last Modified Date: 17.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 17.08.2021
# Last Modified Date: 17.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 17.08.2021
# Last Modified Date: 17.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 17.08.2021
# Last Modified Date: 17.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 17.08.2021
# Last Modified Date: 17.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 17.08.2021
# Last Modified Date: 17.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 17.08.2021
# Last Modified Date: 17.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 17.08.2021
# Last Modified Date: 17.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 17.08.2021
# Last Modified Date: 17.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : views.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
#!/usr/bin/env python


"""MicroBiome Pages.

All the view Related to Microbiome will be will be written herobiome wbe will
be written here.
"""
import numpy as np
import pandas as pd
import random
import string
import os

from .string2query import query2sqlquery

# For pagination
#  from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django_pandas.io import read_frame
from django.conf import settings
from django.shortcuts import render
from django.db.models import Count, F

# from django.db.models.functions import Length
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.decorators.csrf import csrf_exempt

#  from django_tables2.config import RequestConfig
#  from .djmodel import get_model_repr
#  from .models import Movie, Person
from .forms import PostForm
from .models import (
    # BioProject,
    BodySite,
    Disease,
    # LocEthDiet,
    Platform,
    Pubmed,
    Samples,
    # StudyDesign,
)


def random_alnum(size=6):
    """Generate random n character alphanumeric string"""
    # List of characters [a-zA-Z0-9]
    chars = string.ascii_letters + string.digits
    code = "".join(random.choice(chars) for _ in range(size))
    return code


def pie_json(dataframe, column):
    """TODO: Return json for give variable for pie chart.

    :dataframe: data table
    :column: column in table
    :returns: json text

    """
    return (
        dataframe[dataframe["variable"] == column]
        .groupby("value")
        .size()
        .reset_index()
        .rename(columns={"value": "name", 0: "y"})
        .to_json(orient="records")
    )


def date_range(date_list):
    """TODO: return date range if possible.

    :date_list: date in list format
    :returns: range string of date

    """
    if date_list[("value", "amin")] == date_list[("value", "amax")]:
        return f'{date_list[("value", "amin")]}'
    return f'{date_list[("value", "amin")]}:{date_list[("value", "amax")]}'


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
        y=Count("samples__l2bioproject", distinct=True)
    )
    body_site_pie_project = (
        read_frame(body_site_project)
        .rename(columns={"bodysite": "name"})
        .to_json(orient="records")
    )
    body_site_sample = BodySite.objects.all().annotate(y=Count("samples"))
    body_site_pie_sample = (
        read_frame(body_site_sample)
        .rename(columns={"bodysite": "name"})
        .to_json(orient="records")
    )
    # NOTE: ASSAY
    assay_project = (
        Platform.objects.values("assay")
        .annotate(y=Count("samples__l2bioproject", distinct=True))
        .order_by("assay")
    )
    assay_sample = (
        Platform.objects.values("assay")
        .annotate(y=Count("samples", distinct=True))
        .order_by("assay")
    )

    assay_pie_project = (
        read_frame(assay_project)
        .rename(columns={"assay": "name"})
        .to_json(orient="records")
    )
    assay_pie_sample = (
        read_frame(assay_sample)
        .rename(columns={"assay": "name"})
        .to_json(orient="records")
    )

    # NOTE: PLATFORM
    platform_project = (
        Platform.objects.values("platform")
        .annotate(y=Count("samples__l2bioproject", distinct=True))
        .order_by("platform")
    )
    platform_sample = (
        Platform.objects.values("platform")
        .annotate(y=Count("samples", distinct=True))
        .order_by("platform")
    )

    platform_pie_project = (
        read_frame(platform_project)
        .rename(columns={"platform": "name"})
        .to_json(orient="records")
    )
    platform_pie_sample = (
        read_frame(platform_sample)
        .rename(columns={"platform": "name"})
        .to_json(orient="records")
    )

    # NOTE: This code is for future reference, do not delete
    # Body Site
    #      bodysites = BodySite.objects.annotate(y=Count("samples"))
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
    #                            'y': bs.y,
    #                            } for bs in bodysites
    #                            #  'color':color[bs.bodysite]} for bs in bodysites
    #                           if not (bs.bodysite in ["Ebola virus",'nan', 'penil,vaginal'] or 'metagenom' in bs.bodysite)]

    # NOTE: DISEASES

    disease_project = Disease.objects.all().annotate(
        y=Count("samples__l2bioproject", distinct=True)
    )
    disease_sample = Disease.objects.all().annotate(y=Count("samples"))
    disease_pie_project = (
        read_frame(disease_project)
        .rename(columns={"disease": "name"})
        .to_json(orient="records")
    )
    disease_pie_sample = (
        read_frame(disease_sample)
        .rename(columns={"disease": "name"})
        .to_json(orient="records")
    )

    # NOTE: Geographical plotting on map
    geoloc_project = pd.DataFrame(
        Samples.objects.values("longitude", "latitude")
        .annotate(num_project=Count("l2bioproject", distinct=True))
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
                "longitude", "latitude", "l2loc_diet__country")
            .order_by("longitude", "latitude", "l2loc_diet__country")
            .distinct()
        )
    )
    geoloc = (
        geoloc_project.merge(geoloc_sample, on=[
                             "longitude", "latitude"], how="outer")
        .merge(geoloc_country, on=["longitude", "latitude"], how="outer")
        .rename(
            columns={
                "latitude": "lat",
                "longitude": "lon",
                "l2loc_diet__country": "country",
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
        "platform_pie_dict_sample": platform_pie_sample,
        "platform_pie_dict_project": platform_pie_project,
        "records": geoloc,
    }
    # #  print(all_records.values())
    return render(request, "search.html", context)


# https://stackoverflow.com/questions/16458166/how-to-disable-djangos-csrf-validation
@csrf_exempt
def results_sample(request):
    # Try https://github.com/jamespacileo/django-pure-pagination
    if request.method == "GET":
        tags = request.GET.get("tags", None)
        page = request.GET.get("page", 1)
        bioproject = request.GET.get("bioproject", None)
        qs = []
        extras = {}
        if tags:
            tags = f"({tags}) & ({bioproject}[bioproject])"
        else:
            tags = f"({bioproject}[bioproject])"
        query = query2sqlquery(tags)

        # res = Samples.objects.filter(query).values(
        # "sampid",
        # "locetdiet__country",
        # "platform__platform",
        # "amplicon__amplicon",
        # "assay__assay",
        # "disease__disease",
        # "locetdiet__lon",
        # "locetdiet__lat",
        # )
        res = (
            Samples.objects.filter(query)
            .annotate(
                title=F("l2pubmed__title"),
                pubid=F("l2pubmed__pubid"),
                sampleid=F("sampid"),
                bioproject=F("l2bioproject__repoid"),
                country=F("l2loc_diet__country"),
                platform=F("l2platform__platform"),
                assay=F("l2platform__assay"),
                amplicon=F("l2platform__target_amplicon"),
                disease=F("l2disease__disease"),
                lon=F("longitude"),
                lat=F("latitude"),
            )
            .values(
                "sampleid",
                "country",
                "platform",
                "amplicon",
                "assay",
                "disease",
                "lon",
                "lat",
            )
        )
        samples = read_frame(res).fillna("")

        print(samples)
        paginator = Paginator(
            samples.to_dict(orient="records"), 10
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
        platform_pie_dict = (
            read_frame(
                res.values("platform")
                .annotate(y=Count("platform"))
                .order_by("platform")
            )
            .rename(columns={"platform": "name"})
            .to_json(orient="records")
        )
        assay_pie_dict = (
            read_frame(res.values("assay").annotate(
                y=Count("assay")).order_by("assay"))
            .rename(columns={"assay": "name"})
            .to_json(orient="records")
        )

        disease_pie_dict = (
            read_frame(
                res.values("disease").annotate(
                    y=Count("disease")).order_by("disease")
            )
            .rename(columns={"disease": "name"})
            .to_json(orient="records")
        )

        # GEO LOCATION
        try:
            geoloc = read_frame(
                res.values(
                    "lon",
                    "lat",
                    "country",
                    # "project",
                )
                #  LocEthDiet.objects.values(
                #  "lon", "lat","country").annotate(num_samples=Count("samples__project", distinct=True))
            )
            # TODO: Fix country issue with multiple coordinates
            geoloc = (
                geoloc[~(pd.isna(geoloc.lon) | pd.isna(geoloc.lat))]
                .groupby(["lon", "lat", "country"])
                .size()
                .reset_index()
                .rename(columns={0: "num_samples"})
            )
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
    qt, page, tags = "post", 1, None
    if request.method == "POST":
        tags = request.POST["oldsearch"]

    if request.method == "GET":
        tags = request.GET.get("tags", None)
        page = request.GET.get("page", 1)
        qt = "get"

    res = None
    if not tags:
        res = Pubmed.objects.annotate(
            bioproject=F("samples__l2bioproject__repoid"),
            sampleid=F("samples__sampid"),
            country=F("samples__l2loc_diet__country"),
            ethnicity=F("samples__l2loc_diet__ethnicity"),
            ewiki=F("samples__l2loc_diet__el_wiki"),
            platform=F("samples__l2platform__platform"),
            amplicon=F("samples__l2platform__target_amplicon"),
            assay=F("samples__l2platform__assay"),
            disease=F("samples__l2disease__disease"),
            doid=F("samples__l2disease__doid"),
            lon=F("samples__longitude"),
            lat=F("samples__latitude"),
            col_date=F("samples__col_date"),
        ).values(
            "title",
            "pubid",
            "bioproject",
            "sampleid",
            "country",
            "ethnicity",
            "ewiki",
            "platform",
            "amplicon",
            "assay",
            "disease",
            "doid",
            "lon",
            "lat",
            "col_date",
        )
        # print(res)
    else:
        # sql = query2sqlquery(tags)
        query = query2sqlquery(tags)
        res = (
            Samples.objects.filter(query)
            .annotate(
                title=F("l2pubmed__title"),
                pubid=F("l2pubmed__pubid"),
                sampleid=F("sampid"),
                bioproject=F("l2bioproject__repoid"),
                country=F("l2loc_diet__country"),
                ethnicity=F("l2loc_diet__ethnicity"),
                ewiki=F("l2loc_diet__el_wiki"),
                platform=F("l2platform__platform"),
                assay=F("l2platform__assay"),
                amplicon=F("l2platform__target_amplicon"),
                disease=F("l2disease__disease"),
                doid=F("l2disease__doid"),
                lon=F("longitude"),
                lat=F("latitude"),
            )
            .values(
                "title",
                "pubid",
                "bioproject",
                "sampleid",
                "country",
                "ethnicity",
                "ewiki",
                "platform",
                "amplicon",
                "assay",
                "disease",
                "doid",
                "lon",
                "lat",
                "col_date",
            )
        )
    try:
        project_summary = read_frame(
            res.values(
                "pubid",
                "title",
                "bioproject",
                "country",
                "ethnicity",
                "ewiki",
                "disease",
                "doid",
                "platform",
                "assay",
                "amplicon",
                "lon",
                "lat",
                "col_date",
            )
        )
        # print(set(project_summary["ethnicity"]))

        # NOTE: Values with external links
        # Disease ID
        doid = project_summary[["disease", "doid"]].drop_duplicates()
        doid = doid.fillna(0)

        doid = dict(zip(doid.disease, doid.doid))
        del project_summary["doid"]
        # Ethnicity
        ewiki = project_summary[["ethnicity", "ewiki"]]
        ewiki = ewiki[ewiki["ethnicity"] != "nan"].drop_duplicates().fillna(0)
        print(ewiki, "Kiran")
        ewiki = dict(zip(ewiki.ethnicity, ewiki.ewiki))
        del project_summary["ewiki"]

        # TODO: Store information in file to download
        rand_fold = random_alnum()
        result_fold = f"{settings.STATIC_ROOT}/downloads/{rand_fold}"
        if not os.path.exists(result_fold):
            os.makedirs(result_fold, exist_ok=True)
        result_file = f"{result_fold}/results.csv"
        project_summary.to_csv(result_file, index=False)
        result_file = f"downloads/{rand_fold}/results.csv"

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
        project_summary = project_summary.drop(["lon", "lat"], axis=1)

        project_summary = project_summary.melt(id_vars=["pubid", "title"])

        project_summary = project_summary[
            ~(pd.isna(project_summary["value"]) |
              project_summary["value"] == "nan")
        ]
        # NOTE: Pie codes
        platform_pie_dict_sample = pie_json(project_summary, "platform")
        disease_pie_dict_sample = pie_json(project_summary, "disease")
        assay_pie_dict_sample = pie_json(project_summary, "assay")

        # print(platform_pie_dict_sample)
        project_summary_col_date = project_summary.loc[
            project_summary["variable"] == "col_date", ["pubid", "value"]
        ].groupby("pubid")
        project_summary_col_date = project_summary_col_date.agg(
            {"value": [np.min, np.max]}
        )  # .reset_index()
        project_summary_col_date["col_date"] = project_summary_col_date.apply(
            date_range, axis=1
        )
        project_summary_col_date = project_summary_col_date.reset_index()
        print(project_summary_col_date)

        project_summary = (
            project_summary[project_summary["variable"] != "col_date"]
            .groupby(["pubid", "title", "variable", "value"])
            .size()
            .reset_index()
        )
        # project_summary.loc[project_summary["variable"] == "disease", "value"].apply(
        # lambda x: print(x, doid[x])
        # )

        # NOTE: Adding external link related values
        # DOID
        project_summary.loc[project_summary["variable"] == "disease", "value"] = (
            # print(
            project_summary.loc[project_summary["variable"]
                                == "disease", "value"]
            .apply(lambda x: tuple([x, doid[x]]))
            .values
        )
        # ETHNICITY WIKI

        def ethni(ewiki, key):
            """TODO: Docstring for ethni.

            :key: TODO
            :returns: TODO

            """
            try:
                return tuple([key, ewiki[key]])
            except:
                return False

        project_summary.loc[project_summary["variable"] == "ethnicity", "value"] = (
            # # print(
            project_summary.loc[project_summary["variable"]
                                == "ethnicity", "value"]
            .apply(lambda x: ethni(ewiki, x))
            .values
        )
        print(
            set(project_summary["value"]),
            # project_summary[~project_summary["value"]],
        )
        project_summary = project_summary[project_summary["value"] != False]
        print(project_summary)

        # project_summary["value"] = project_summary["value"] + \
        # "("+project_summary[0].astype(str)+")"
        project_summary["value"] = project_summary[["value", 0]].apply(
            lambda x: {x["value"]: x[0]}, axis=1
        )
        print(project_summary)
        # TODO: Use dictionary
        del project_summary[0]
        # project_summary = project_summary.groupby(["pubid", "title", "variable"])[
        # "value"].apply(lambda x: ",".join(x.values)).reset_index()

        project_summary = (
            project_summary.groupby(["pubid", "title", "variable"])["value"]
            .apply(list)
            .reset_index()
        )

        # print(project_summary)
        project_summary["value"] = project_summary["value"].apply(mergedict)

        # NOTE: Calculating date range
        # project_summary.loc[
        # project_summary["variable"] == "col_date", "value"
        # ] = project_summary.loc[
        # project_summary["variable"] == "col_date", "value"
        # ].apply(
        # date_range
        # )
        project_summary = project_summary.pivot(
            index=["pubid", "title"], columns="variable", values="value"
        ).reset_index()
        project_summary = (
            project_summary.merge(
                project_summary_col_date[["pubid", "col_date"]], on="pubid"
            )
            .rename(columns={("col_date", ""): "col_date"})
            .fillna(False)
        )

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
                "items": items,
                "result_file": result_file
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
                "items": items,
                "result_file": result_file
                # 'query': query[: -1]
            },
        )
    # else:
    #     response = redirect('/search/')
    #     return response


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
