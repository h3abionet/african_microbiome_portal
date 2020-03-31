#!/usr/bin/env python


"""MicroBiome Pages.

All the view Related to Microbiome will be will be written herobiome wbe will
be written here.
"""

import numpy as np
import pandas as pd
# For pagination
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count, Q
from django.shortcuts import render
from django_pandas.io import read_frame
from django_tables2 import RequestConfig

#  from django_tables2.config import RequestConfig
from .djmodel import get_model_repr
# Create your views here.
#  from .models import Movie, Person
from .forms import PostForm, Upload
from .models import Project


#  from django.template import Context, loader
# https://docs.djangoproject.com/en/3.0/topics/http/file-uploads/
def _savefile(infile):
    with open("test.txt","wb+") as fout:
        for chunk in infile.chunks():
            fout.write(chunk)




def upload_file(request):
    if request.method == 'POST':
        #  print("Kiran")
        formx = Upload(request.POST, request.FILES)
        #  print(request)
        if formx.is_valid():
            _ = _savefile(request.FILES['infile'])
            sep = formx.data["separator"]
            #  print("Anmol", sep)
            try:
                is_csv = len(open("test.txt").readline().split(sep))
                if not is_csv:
                    return render(request, 'warning2.html', {})
                df = pd.read_csv("test.txt",sep=sep)
                # Must have colums
                must_have_colums =  set(["REPOSITORY ID",
                                      "STUDY TITLE",
                                      #  "REPOSITORY LINK",
                                      "SAMPLE NUMBER",
                                      "STUDY LINK",
                                      "ASSAY TYPE",
                                      "TECHNOLOGY",
                                      "COUNTRY",
                                      "DISEASE",
                                      "STUDY DESIGN",
                                      "BODY SITE",
                                      "PLATFORM",
                                      "PARTICIPANT FEATURES",
                                      #  "AVERAGE SPOTLENGTH",
                                      "LIBRARY LAYOUT",
                                      "LON LAT",
                                      "SAMPLE TYPE",
                                      "COLLECTION DATE",
                                      "ETHNICITY",
                                      "URBANZATION",
                                      "REGION",
                                      "CITY",
                                      "TARGET AMPLICON",
                                      "DIET"
                                      ])
                column_not_found = must_have_colums - set(df.columns)
                if column_not_found:
                    return render(request, 'warning.html', {'columns':column_not_found})
                    #  print(column_not_found)
                df_dict = {}
                # Add separate value for the location
                # Check if the value already exists in the table. If it does, mark with star
                for col in must_have_colums:
                    #  print(col)
                    # Unknown
                    col_val = Project.objects.order_by().values_list(col.replace(" ", "_").lower()).distinct()
                    #  print(col_val)
                    updated_list = []
                    for val in set(df[col]):
                        if (val,) in col_val:
                            updated_list.append(str(val))
                        else:
                            updated_list.append(str(val)+"*")
                    df_dict[col] = updated_list
                return render(request,'overview.html', {'results':df_dict})
            except:
                return render(request, 'warning2.html', {})

    else:
        formx = Upload()
    return render(request,"uploads.html",{'form':formx})

# Create your views here.




def front_main(request):
    """Show front page of the website.
    """
    print(Person.nodes.all())
    #  return render(request, "MicroBiome/search.html", {})
    return render(request, "MicroBiome/results.html", {'movies': Movie.nodes.all()})


def test_update():
    df = pd.read_csv("/home/devil/Documents/Tools/Database/Data/test.csv")
    predef_names = set(['REPOSITORY ID', 'STUDY TITLE', 'STUDY LINK', 'ASSAY TYPE',
       'TECHNOLOGY', 'COUNTRY', 'DISEASE', 'STUDY DESIGN', 'BODY SITE',
       'PLATFORM', 'PARTICIPANT FEATURES', 'LIBRARY LAYOUT', 'LON LAT',
       'SAMPLE TYPE', 'COLLECTION DATE', 'ETHNICITY', 'URBANZATION', 'REGION',
       'CITY', 'TARGET AMPLICON', 'DIET', 'SAMPLE NUMBER'])
    if len(predef_names-set(df.columns)):
        print(predef_names-set(df.columns), "are not table columns names in gven table")
        #  exit("Exiting.....")
    for _, row in df.iterrows():
        print(row)
        #  continue
        #  print(row['repository'])
        created = Project.objects.get_or_create(
            repository_id=row["REPOSITORY ID"],  # max length was 11
            study_title=row["STUDY TITLE"],
            study_link=row["STUDY LINK"],
            assay_type=row["ASSAY TYPE"],
            technology=row['TECHNOLOGY'],
            country=row["COUNTRY"],
            disease=row["DISEASE"],
            study_design=row["STUDY DESIGN"],
            body_site=row["BODY SITE"],
            platform=row["PLATFORM"],
            participant_features = row['PARTICIPANT FEATURES'],
            library_layout = row['LIBRARY LAYOUT'],
            lon_lat = row['LON LAT'],
            sample_type=row["SAMPLE TYPE"],
            collection_date = row["COLLECTION DATE"],
            ethnicity = row['ETHNICITY'],
            urbanzation = row["URBANZATION"],
            region = row["REGION"],
            city = row["CITY"],
            target_amplicon = row["TARGET AMPLICON"],
            diet = row["DIET"],
            sample_number=row["SAMPLE NUMBER"]
        )

    #  df = pd.read_csv(
    #      "/home/devil/Documents/Tools/Database/MicroBiome/test.csv")
    #
    #  for _, row in df.iterrows():
    #      print(row)
    #      #  print(row['repository'])
    #      created = Project.objects.get_or_create(
    #          sample_count=row["SAMPLE_COUNT"],
    #          repository_id=row["REPOSITORY_ID"],  # max length was 11
    #          study_title=row["STUDY_TITLE"],
    #          study_link=row["STUDY_LINK"],
    #          assay_type=row["ASSAY_TYPE"],
    #          platform=row["PLATFORM"],
    #          country=row["COUNTRY"],
    #          disease=row["DISEASE"],
    #          study_design=row["STUDY_DESIGN"],
    #          body_site=row["BODY_SITE"],
    #          lon=row["LON"],
    #          lat=row["LAT"],
    #          repo=row["REPO"],
    #          sample_type=row["SAMPLE_TYPE"],
    #      )
    #
    #
#  def search_form(request):
#      return render(request, "mainLayout.html", {})
#
def search_form(request):
    form = PostForm()
    #  test_update()
    #  print(form.as_p, "Anmol")
    all_records=Project.objects.all()
    df = read_frame(all_records)
    df = df.loc[:, #~(pd.isnull(df.lat) | pd.isnull(df.lon)),
            ['lon_lat', 'sample_type', 'disease','platform',
                'country','sample_number', 'body_site','assay_type']]
    dft = df.groupby("body_site")['sample_number'].apply(np.sum).reset_index()
    print(dft.head())
    site_pie_dict = [{'name': item['body_site'],
                        'y': item['sample_number']} for _, item in dft.iterrows()]
    #  print(site_pie_dict)

    dft = df.groupby("platform")['sample_number'].apply(np.sum).reset_index()
    platform_pie_dict = [{'name': item['platform'], 'y': item['sample_number'] } for _, item in dft.iterrows()]

    assay_type = df.groupby("assay_type")['sample_number'].apply(np.sum).reset_index()
    #  assay_type=pd.DataFrame(list(all_records.values('assay_type').annotate(type_count=Count('sample_type'))))
    xdata_assay=list(assay_type['assay_type'])
    ydata_assay=list(assay_type['sample_number'])

    disease = df.groupby("disease")['sample_number'].apply(np.sum).reset_index()
    #  disease=pd.DataFrame(list(all_records.values('disease').annotate(type_count=Count('disease'))))
    xdata_disease=list(disease['disease'])
    ydata_disease=list(disease['sample_number'])
    dft = df[df["lon_lat"]!="unknown"]
    #  print(set(dft["lon_lat"]))
    dft["lon"] = dft["lon_lat"].apply(lambda x: x.split(",")[0])
    dft["lat"] = dft["lon_lat"].apply(lambda x: x.split(",")[1])
    #  print("anmol")

    context={'form':form,
            'xdata_assay': xdata_assay,
            'ydata_assay': ydata_assay,
            'xdata_disease': xdata_disease,
            'ydata_disease': ydata_disease,
            'platform_pie_dict': platform_pie_dict,
            'site_pie_dict': site_pie_dict,
            'records': dft};
    #  print(all_records.values())
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
#


def results(request):
    # Try https://github.com/jamespacileo/django-pure-pagination
    if request.method == "GET":
        form = PostForm(request.GET)

        try:
            tags = form.data["tags"]
            tags = tags.split(",")
        except KeyError:
            tags = None

        if not tags:
            res = Project.objects.all()
        else:
            qs = [
                    #  Q(country__icontains=tag)|
                    #  Q(platform__icontains=tag)|
                    #  Q(disease__icontains=tag)|
                    #  Q(study_design__icontains=tag)|
                    #  Q(study_title__icontains=tag)|
                    #  Q(sample_type__icontains=tag)
                  Q(repository_id__icontains=tag)|
                  Q(study_title__icontains=tag)|
                  Q(study_link__icontains=tag)|
                  Q(assay_type__icontains=tag)|
                  Q(technology__icontains=tag)|
                  Q(country__icontains=tag)|
                  Q(disease__icontains=tag)|
                  Q(study_design__icontains=tag)|
                  Q(body_site__icontains=tag)|
                  Q(platform__icontains=tag)|
                  Q(participant_features__icontains=tag)|
                  Q(library_layout__icontains=tag)|
                  Q(lon_lat__icontains=tag)|
                  Q(sample_type__icontains=tag)|
                  Q(collection_date__icontains=tag)|
                  Q(ethnicity__icontains=tag)|
                  Q(urbanzation__icontains=tag)|
                  Q(region__icontains=tag)|
                  Q(city__icontains=tag)|
                  Q(target_amplicon__icontains=tag)|
                  Q(diet__icontains=tag)|
                  Q(sample_number__icontains=tag)
                    for tag in tags]
            query = qs.pop()
            for q in qs:
                query |= q

            res = Project.objects.filter(query)
        df = read_frame(res)
        del df['id']
        df2 = {}
        for col in df.columns:
            df2[col] = []
            for repid in set(df['repository_id']):
                # TODO: Correct mgp12183  database links
                if col not in ['repository_id','study_title', 'sample_number']:
                    val = ";".join([f"<a href='/microbiome/results/?tags={val}'>{val}</a>" for val in map(str, list(set(df.loc[df['repository_id']==repid, col].values)))])
                else:
                    val = ";".join(map(str, list(set(df.loc[df['repository_id']==repid, col].values))))
                df2[col].append(val)
        del df
        df2 = pd.DataFrame(df2)
        print(set(df2["diet"]))

        res_count = len(res)
        query = ""
        for k, v in form.data.items():
            query += "%s=%s&" % (k, v)
        return render(request, "results.html", {'results': df2, 'res_count': res_count,  'query': query[:-1]})
    else:
        form = PostForm()

        all_records=Project.objects.all()
        df = read_frame(all_records)
        df = df.loc[~(pd.isnull(df.lat) | pd.isnull(df.lon)),
                ['lon', 'lat', 'sample_type', 'disease','platform',
                    'country','sample_count']]
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
        print("anmol")

        context={#'form':form,
                'xdata_assay': xdata_assay,
                'ydata_assay': ydata_assay,
                'xdata_disease': xdata_disease,
                'ydata_disease': ydata_disease,
                'platform_pie_dict': platform_pie_dict,
                'site_pie_dict': site_pie_dict,
                'records': df};
        #  print(all_records.values())
        return render(request, "search.html", context=context)

        #  return render(request, 'dashboard.html', context=context)



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

def summary(request):
    all_records=Project.objects.all()
    df = read_frame(all_records)
    df = df.loc[~(pd.isnull(df.lat) | pd.isnull(df.lon)),
            ['lon', 'lat', 'sample_type', 'disease','platform',
                'country','sample_count']]
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
            'records': df};
    #  print(all_records.values())

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
