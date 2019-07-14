#!/usr/bin/env python


"""MicroBiome Pages.

All the view Related to Microbiome will be will be written herobiome wbe will
be written here.
"""

import pandas as pd

# For pagination
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

#  import django_tables2 as tables
#  from django_tables2.config import RequestConfig
from .djmodel import get_model_repr
# Create your views here.
#  from .models import Movie, Person
from .forms import PostForm
from .models import Project

#  from django.template import Context, loader


# Tables # Might need to be moved to new File


#  class ProjectTable(tables.Table):
#      class Meta:
#          model = Project
#

##


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
    form = PostForm()
    #  test_update()
    print(form.as_p, "Anmol")
    return render(request, "search.html", {"form": form})


def results_download(request):
    if request.method == "GET":
        form = PostForm(request.GET)
        print("Anmol", form)
        if form.is_valid():
            print("Kiran")
        country = form.cleaned_data["country"]
        #  page = request.GET.get('page', 1)
        res = Project.objects.filter(country__icontains=country)
        csv = pd.DataFrame(list(res.values()))
        print(csv)
        csv = csv.to_csv(index=False)
        print(csv)
        return render(request, "csv.html", {'csv': csv})


def results(request):
    # Try https://github.com/jamespacileo/django-pure-pagination
    if request.method == "GET":
        form = PostForm(request.GET)
        if form.is_valid():
            print("Kiran", form.cleaned_data)
        country = form.cleaned_data["country"]
        #  page = request.GET.get('page', 1)
        res = Project.objects.filter(country__icontains=country)
        #  df = pd.DataFrame(list(res.values()))
        #  print(df.head().to_csv())

        res_count = len(res)
        #  paginator = Paginator(res, 10)
        query = ""
        for k, v in form.cleaned_data.items():
            query += "%s=%s&" % (k, v)
        return render(request, "results.html", {'results': res, 'res_count': res_count,  'query': query[:-1]})
    else:
        form = PostForm()
        return render(request, "search.html", {"form": form})


def results2(request):
    # Try https://github.com/jamespacileo/django-pure-pagination
    if request.method == "GET":
        #  print("anmol")
        form = PostForm(request.GET)
        if form.is_valid():
            print("Kiran", form.cleaned_data)
        country = form.cleaned_data["country"]
        page = request.GET.get('page', 1)
        resfull = Project.objects.filter(country__icontains=country)
        #  print(len(res))
        paginator = Paginator(resfull, 10)
        query = ""
        for k, v in form.cleaned_data.items():
            query += "%s=%s&" % (k, v)
        try:
            res = paginator.page(page)
        except PageNotAnInteger:
            res = paginator.page(1)
        except EmptyPage:
            res = paginator.page(paginator.num_pages)
        # https://django-endless-pagination.readthedocs.io/en/latest/twitter_pagination.html
        # https://samulinatri.com/blog/django-pagination-tutorial/
        # Toggle columns: https://www.w3schools.com/jquerymobile/tryit.asp?filename=tryjqmob_tables_columntoggle
        return render(request, "results_infinit.html", {'results': res, 'res_count': len(resfull), 'query': query})
    else:
        form = PostForm()
        return render(request, "search.html", {"form": form})



def summary(request):
    all_records=Project.objects.all()
    site_pie_dict = [{'name': item['body_site'],
                        'y': item['type_count'] } for item in all_records.values('body_site').annotate(type_count=Count('body_site')) ]

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
            'all_records': all_records};

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
