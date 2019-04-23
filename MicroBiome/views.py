#!/usr/bin/env python


"""MicroBiome Pages.

All the view Related to Microbiome will be will be written herobiome wbe will
be written here.
"""

import pandas as pd
# For pagination
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

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
    df = pd.read_csv("./testdata/Feuil2.csv")

    for _, row in df.iterrows():
        print(row)
        print(row['repository'])
        created = Project.objects.get_or_create(
            repository=row['repository'],
            study_title=row['study_title'],
            pmid=row['pmid'],
            assay_type=row['assay_type'],
            avg_spotlen=row['avg_spotlen'],
            bioproject_name=row['bioproject_name'],
            bioproject=row['bioproject'],
            bioproject_links=row['bioproject_links'],
            mg_id=row['mg_id'],
            biosample=row['biosample'],
            # Please do not use dash(-), Please use underscore
            mg_rast_id=row['mg-rast_id'],
            biosample_model=row['biosample_model'],
            run=row['run'],
            sra_sample=row['sra_sample'],
            sra_study=row['sra_study'],
            sample_name=row['sample_name'],
            collection_date=row['collection_date'],
            experiment=row['experiment'],
            library_source=row['library_source'],
            library_layout=row['library_layout'],
            libraryselection=row['libraryselection'],
            insert_size=row['insert_size'],
            library_name=row['library_name'],
            centre_name=row['centre_name'],
            instrument=row['instrument'],
            platform=row['platform'],
            amplicon_target=row['amplicon_target'],
            load_date=row['load_date'],
            release_date=row['release_date'],
            ena_last_update=row['ena_last_update'],
            mbases=row['mbases'],
            mbytes=row['mbytes'],
            organism=row['organism'],
            env_biome=row['env_biome'],
            env_feature=row['env_feature'],
            env_material=row['env_material'],
            country=row['country'],
            host=row['host'],
            case_control=row['case_control'],
            host_taxa_id=row['host_taxa_id'],
            lat_ion=row['lat_ion'],
            latitude=row['latitude'],
            longitude=row['longitude'],
            coordinate=row['coordinate'],
            physical_specimen_remaining=row['physical_specimen_remaining'],
            pregnant=row['pregnant'],
            consent=row['consent'],
            datastore_provider=row['datastore_provider'],
            isolation_source=row['isolation_source'],
            sex=row['sex'],
            antibiotic_regimen=row['antibiotic_regimen'],
            birth_delivery=row['birth_delivery'],
            special_diet=row['special_diet'],
            disease_stage=row['disease_stage'],
            host_body_mass_index=row['host_body_mass_index'],
            fastq_ftp=row['fastq_ftp'],
            bp_count=row['bp_count'],
            seq_count=row['seq_count'])


def search_form(request):
    form = PostForm()
    #  test_update()
    print(form.as_p, "Anmol")
    return render(request, "MicroBiome/search.html", {"form": form})


def results(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            country = form.cleaned_data["country"]
            res = Project.objects.filter(country__icontains=country)
            page = request.GET.get('page', 1)
            paginator = Paginator(res, 10)
            # TODO: configure pagegination
            #  print(form.cleaned_data["study_title"])
            #  print(form.cleaned_data["assay_type"])

            return render(request, "MicroBiome/results.html", {'results': res})
        return render(request, "MicroBiome/search.html", {})
        #  return "Anmol"
    else:
        return render(request, "MicroBiome/search.html", {})


def about(request):
    """The Database Introduction Page.
    """
    return render(request, "MicroBiome/about.html", {})
