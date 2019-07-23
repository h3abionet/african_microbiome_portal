#!/usr/bin/env python


"""MicroBiome Pages.

All the view Related to Microbiome will be will be written herobiome wbe will
be written here.
"""

import pandas as pd

# For pagination
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count
from django.shortcuts import render
from django_tables2 import RequestConfig

#  from django_tables2.config import RequestConfig
from .djmodel import get_model_repr
# Create your views here.
#  from .models import Movie, Person
from .forms import PostForm
from .models import Project

#  from django.template import Context, loader





def front_main(request):
    """Show front page of the website.
    """
    print(Person.nodes.all())
    #  return render(request, "MicroBiome/search.html", {})
    return render(request, "MicroBiome/results.html", {'movies': Movie.nodes.all()})


def test_update():
    df = pd.read_csv(
        "/home/devil/Documents/Tools/Database/MicroBiome/test.csv")

    for _, row in df.iterrows():
        print(row)
        #  print(row['repository'])
        created = Project.objects.get_or_create(
            sample_count=row["SAMPLE_COUNT"],
            repository_id=row["REPOSITORY_ID"],  # max length was 11
            study_title=row["STUDY_TITLE"],
            study_link=row["STUDY_LINK"],
            assay_type=row["ASSAY_TYPE"],
            platform=row["PLATFORM"],
            country=row["COUNTRY"],
            disease=row["DISEASE"],
            study_design=row["STUDY_DESIGN"],
            body_site=row["BODY_SITE"],
            lon=row["LON"],
            lat=row["LAT"],
            repo=row["REPO"],
            sample_type=row["SAMPLE_TYPE"],
        )


#  def search_form(request):
#      return render(request, "mainLayout.html", {})
#
def search_form(request):
    form = PostForm(initial={'country':'',
                            'platform':'',
                            'disease':'',
                            'study_design':''})
    #  test_update()
    #  print(form.as_p, "Anmol")
    return render(request, "search.html", {"form": form})


def results_download(request):
    if request.method == "GET":
        form = PostForm(request.GET)
        print("Anmol", form)
        if form.is_valid():
            print("Kiran")
        country = form.cleaned_data["country"]
        platform = form.cleaned_data["platform"]
        disease = form.cleaned_data["disease"]
        study_design = form.cleaned_data["study_design"]
        #  page = request.GET.get('page', 1)
        res = Project.objects.all()
        if country:
            res = res.filter(country__icontains=country)
        if platform:
            res = res.filter(platform__icontains=country)
        if disease:
            res = res.filter(disease__icontains=country)
        if study_design:
            res = res.filter(study_design__icontains=country)
        csv = pd.DataFrame(list(res.values()))
        print(csv)
        csv = csv.to_csv(index=False)
        print(csv)
        return render(request, "csv.html", {'csv': csv})


def results(request):
    # Try https://github.com/jamespacileo/django-pure-pagination
    if request.method == "GET":
        form = PostForm(request.GET)
        #  print(form.cleaned_data)
        #  if form.is_valid():
        #      print("Kiran", form.cleaned_data)
        print(form.data['country'])

        country = form.data["country"]
        platform = form.data["platform"]
        disease = form.data["disease"]
        study_design = form.data["study_design"]
        #  page = request.GET.get('page', 1)
        res = Project.objects.all()
        if country:
            res = res.filter(country__icontains=country)
        if platform:
            res = res.filter(platform__icontains=platform)
        if disease:
            res = res.filter(disease__icontains=disease)
        if study_design:
            res = res.filter(study_design__icontains=study_design)


        res_count = len(res)
        query = ""
        for k, v in form.data.items():
            query += "%s=%s&" % (k, v)
        return render(request, "results.html", {'results': res, 'res_count': res_count,  'query': query[:-1]})
    else:
        form = PostForm()
        return render(request, "search.html", {"form": form})





def summary(request):
    all_records=Project.objects.all()
    site_pie_dict = [{'name': item['body_site'],
                        'y': item['type_count']} for item in \
                                all_records.values('body_site')\
                                .annotate(type_count=Count('body_site')) ]
    #  print(site_pie_dict)

    platform_pie_dict = [{'name': item['platform'], 'y': item['type_count'] } for item in all_records.values('platform').annotate(type_count=Count('sample_type')) ]

    assay_type=pd.DataFrame(list(all_records.values('assay_type').annotate(type_count=Count('sample_type'))))
    xdata_assay=list(assay_type['assay_type'])
    ydata_assay=list(assay_type['type_count'])

    disease=pd.DataFrame(list(all_records.values('disease').annotate(type_count=Count('disease'))))
    xdata_disease=list(disease['disease'])
    ydata_disease=list(disease['type_count'])

    context={'xdata_assay': xdata_assay,
            'ydata_assay': ydata_assay,
            'xdata_disease': xdata_disease,
            'ydata_disease': ydata_disease,
            'platform_pie_dict': platform_pie_dict,
            'site_pie_dict': site_pie_dict,
            'all_records': all_records.values()};
    print(all_records.values())

    return render(request, 'dashboard.html', context=context)


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
