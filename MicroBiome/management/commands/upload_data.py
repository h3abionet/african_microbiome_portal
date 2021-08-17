#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
# -*- coding: utf-8 -*-
# File              : upload_data.py
# Date              : 16.08.2021
# Last Modified Date: 16.08.2021
import re
import sys


import numpy as np
import pandas as pd

from geopy.geocoders import Nominatim
from django_pandas.io import read_frame
from django.core.management.base import BaseCommand, CommandError

from MicroBiome import models
from MicroBiome.date2date import to_date


def remove_multiple_spaces(txt):
    """Removes multiple spaces from the text and strip spaces at the ends."""
    return re.sub(" +", " ", txt).strip()


# TODO: Create a function for many-to-many relation


def multi_value_columns_rows_allowed(dataframe):
    """TODO: Docstring for multi_value_columns_rows_allowed.
    :returns: TODO

    """
    for col in [
        "DISEASE",
        "ELO",
        "DOID",
        "ETHNICITY",
        "REGION",
        "LAT LON",
        "URBANZATION",
        "CITYVILLAGE",
        "COUNTRY",
        "TARGET AMPLICON",
    ]:
        dataframe = dataframe[
            dataframe[col].apply(lambda x: len(str(x).split("//"))) < 2
        ]
    return dataframe


def update_pubmed(pubmed_info):
    """TODO: Docstring for upload_pubmed.

    :pubmed_info: TODO
      :returns: TODO

    """
    # NOTE: Title will be selected based on first occurance of the pubid
    # NOTE: Later instances will be ignored.
    pubmed_dict = {}
    for i, info in enumerate(pubmed_info):
        try:
            query = models.Pubmed.objects.get(pubid=info[1])
        except:
            query = models.Pubmed.objects.create(title=info[0], pubid=info[1])
        pubmed_dict[info[1]] = query
        # break
    return pubmed_dict


def update_bioproject(bioprojects, study_dict):
    """TODO: Docstring for update_bioproject.

    :arg1: TODO
    :returns: TODO

    """
    bioproject_dict = {}
    for _, bioproject in bioprojects.iterrows():
        try:
            query = models.BioProject.objects.get(
                repoid=bioproject["REPOSITORY ID"])
        except:
            query = models.BioProject.objects.create(
                repoid=bioproject["REPOSITORY ID"])
            study_str = bioproject["STUDY DESIGN"]
            if type(study_str) == str:
                study_list = study_str.split("//")
                for study in study_list:
                    print(study, study_dict)
                    query.study_design.add(
                        study_dict[remove_multiple_spaces(study)])
            query.save()
        bioproject_dict[bioproject["REPOSITORY ID"]] = query
    return bioproject_dict


def update_study_design(study_design_info):
    """TODO: Docstring for study_design.

    :study_design_info: TODO
    :returns: TODO

    """
    studies_dict = {}
    for studties_str in study_design_info:
        studies_list = studties_str.split("//")
        for study in studies_list:
            query = models.StudyDesign.objects.get_or_create(
                study_design=remove_multiple_spaces(study)
            )[0]
            studies_dict[remove_multiple_spaces(study)] = query
    return studies_dict


def upate_disease(disease_info):
    """TODO: Docstring for disease.

    :arg1: TODO
    :returns: TODO

    """
    disease_dict = {}
    for info in disease_info:
        # print(i, info)
        query = models.Disease.objects.get_or_create(
            disease=info[0], doid=info[1])[0]
        disease_dict[info[0]] = query
    return disease_dict


def update_bodysite(bodysites):
    """TODO: Docstring for check_bodysite.

    :bodysites: TODO
    :returns: TODO

    """
    body_site_dict = {}
    for bodysite in bodysites:
        query = models.BodySite.objects.get_or_create(bodysite=bodysite)[0]
        body_site_dict[bodysite] = query
    return body_site_dict


def project_summary():
    """TODO: Docstring for project_summary.
    :returns: TODO

    """
    # TODO: Just update the table and the end of the run of update of the data
    pass


def sequenced_region(seq_regions):
    """TODO: Docstring for sequenced_region.

    :seq_regions: TODO
    :returns: TODO

    """
    # TODO: Revove v from the sequence names
    pass


def update_platform(platform):
    """Checking info in pubmed table."""
    platform_dict = {}
    for _, info in platform.iterrows():
        print(info.values)
        query = models.Platform.objects.get_or_create(
            platform=info["PLATFORM"],
            technology=info["TECHNOLOGY"],
            assay=None if info["ASSAY TYPE"] == np.nan else info["ASSAY TYPE"],
            target_amplicon=None
            if info["TARGET AMPLICON"] == np.nan
            else info["TARGET AMPLICON"],
        )[0]
        platform_dict[tuple(info.values)] = query
    return platform_dict


def update_samples(
    samples,
    pub_dict,
    plt_dict,
    body_site_dict,
    disease_dict,
    loc_diet_dict,
    bioproject_dict,
):
    """TODO: Docstring for check_bodysite.

    :bodysites: TODO
    :returns: TODO

    """
    # NOTE: In case of duplication of samples, first occurance information will
    "Run ID"
    "AVERAGE SPOTLENGTH"
    "COLLECTION DATE"
    "LIBRARY LAYOUT"
    "LAT LON"

    for _, sample in samples.iterrows():
        # print(sample)
        try:
            query = models.Samples.objects.get(sampid=sample["Run ID"])
            # NOTE: Pubid integration
            pubids = [
                int(remove_multiple_spaces(pid))
                for pid in sample["STUDY LINK"].split("//")
            ]
            # print(pubids, "Alpha", pub_dict[pubids[0]])
            # print(read_frame(query), "Anmol")
            for pubid in pubids:
                query.l2pubmed.add(pub_dict[pubid])

        except:
            query = models.Samples.objects.create(
                sampid=sample["Run ID"],
                avspotlen=sample["AVERAGE SPOTLENGTH"],
                col_date=sample["COLLECTION DATE"],
                lib_layout=sample["LIBRARY LAYOUT"],
                longitude=sample["LON"],
                latitude=sample["LAT"],
                capital=sample["CAPITAL"],
            )
            # NOTE: Pubid integration
            pubids = [
                int(remove_multiple_spaces(pid))
                for pid in sample["STUDY LINK"].split("//")
            ]
            # print(pubids, "Alpha", pub_dict[pubids[0]])
            # print(read_frame(query), "Anmol")
            for pubid in pubids:
                query.l2pubmed.add(pub_dict[pubid])
                # print("K", sample["Run ID"], pubid)

            # NOTE: Platform information integration
            # print(plt_dict[(sample[6], sample[7], sample[8])],
            # (sample[6], sample[7], sample[8]))
            query.l2platform = plt_dict[
                (
                    sample["PLATFORM"],
                    sample["TECHNOLOGY"],
                    sample["ASSAY TYPE"],
                    sample["TARGET AMPLICON"],
                )
            ]

            # NOTE: Body site integration
            query.l2bodysite = body_site_dict[sample["BODY SITE"].upper()]

            # NOTE: Disease information integration
            if type(sample["DISEASE"]) == str:
                print(type(sample["DISEASE"]), disease_dict)
                diseases = [
                    remove_multiple_spaces(disease)
                    for disease in sample["DISEASE"].split(",")
                ]
                for disease in diseases:
                    query.l2disease.add(disease_dict[disease.upper()])
                if len(diseases) > 1:
                    query.is_mixed = True
            # NOTE: Loc and diets related information integration
            query.l2loc_diet = loc_diet_dict[
                tuple(
                    sample[
                        [
                            "COUNTRY",
                            "REGION",
                            "CITYVILLAGE",
                            "URBANZATION",
                            "ETHNICITY",
                            "ELO",
                            "WIKI",
                            "DIET",
                        ]
                    ].values
                )
            ]
            query.l2bioproject = bioproject_dict[sample["REPOSITORY ID"]]

            query.save()
            # exit(0)


# Diet and geographical location
# return


def update_loc_diet(loc_diet):
    """TODO: Docstring for check_loc_diet.

    :loc_diet_info: TODO
    :returns: TODO

    """

    loc_diet_info_dict = {}
    for _, info in loc_diet.iterrows():
        query = models.LocEthDiet.objects.get_or_create(
            country=info["COUNTRY"],
            region=None if info["REGION"] == np.nan else info["REGION"],
            urbanization=None if info["URBANZATION"] == np.nan else info["URBANZATION"],
            cityvillage=None if info["CITYVILLAGE"] == np.nan else info["CITYVILLAGE"],
            ethnicity=None if info["ETHNICITY"] == np.nan else info["ETHNICITY"],
            elo=None if info["ELO"] == np.nan else info["ELO"],
            el_wiki=None if info["WIKI"] == np.nan else info["WIKI"],
            diets=None if info["DIET"] == np.nan else info["DIET"],
        )[0]
        loc_diet_info_dict[tuple(info.values)] = query
    return loc_diet_info_dict


def lan_lot(coor):
    """Return coordinate information

    :coor: TODO
    :returns: TODO

    """
    capital = False
    if coor.endswith("*"):
        capital = True
        coor = coor[:-1]
    lan, lot = coor.split(",")
    return float(lan.strip()), float(lot.strip()), capital


class Command(BaseCommand):

    """Docstring for Command."""

    def __init__(self):
        """TODO: to be defined."""
        BaseCommand.__init__(self)

    def add_arguments(self, parser):
        parser.add_argument("--infile", type=str,
                            help="Input csv file to be tested")

    def handle(self, *args, **options):
        """TODO: Docstring for function.

        :arg1: TODO
        :returns: TODO

        """
        infile = options["infile"]
        if not infile:
            print("Infput file not given. Exiting . . . . .")
            sys.exit(0)
        # NOTE: Columns to be used
        usecols = [
            "REPOSITORY ID",
            # "REPOSITORY LINK",
            "SAMPLE NUMBER",
            "STUDY TITLE",
            "STUDY LINK",
            "ASSAY TYPE",
            "TECHNOLOGY",
            "COUNTRY",
            "DISEASE",
            "DOID",
            "STUDY DESIGN",
            "BODY SITE",
            "PLATFORM",
            "PARTICIPANT FEATURES",
            "AVERAGE SPOTLENGTH",
            "Run ID",
            # "Sample ID",
            # "Sample Name",
            "COLLECTION DATE",
            "LIBRARY LAYOUT",
            "LAT LON",
            "SAMPLE TYPE",
            "ETHNICITY",
            "ELO",
            "URBANZATION",
            "REGION",
            "CITYVILLAGE",
            "TARGET AMPLICON",
            "DIET",
        ]
        col_type = {
            "REPOSITORY ID": str,
            # "REPOSITORY LINK",
            "SAMPLE NUMBER": int,
            "STUDY TITLE": str,
            "STUDY LINK": str,
            "ASSAY TYPE": str,
            "TECHNOLOGY": str,
            "COUNTRY": str,
            "DISEASE": str,
            "DOID": str,
            "STUDY DESIGN": str,
            "BODY SITE": str,
            "PLATFORM": str,
            "PARTICIPANT FEATURES": str,
            "AVERAGE SPOTLENGTH": int,
            "Run ID": str,
            # "Sample ID",
            # "Sample Name",
            "COLLECTION DATE": str,
            "LIBRARY LAYOUT": str,
            "LAT LON": str,
            "SAMPLE TYPE": str,
            "ETHNICITY": str,
            "ELO": str,
            "URBANZATION": str,
            "REGION": str,
            "CITYVILLAGE": str,
            "TARGET AMPLICON": str,
            "DIET": str,
        }

        # NOTE: Reporting error if required columns are not in the given file
        data = pd.read_csv(infile, usecols=usecols, dtype=col_type)
        print(data[["COLLECTION DATE"]].head())
        data["COLLECTION DATE"] = data["COLLECTION DATE"].apply(to_date)
        # not_found_column = set(usecols) - set(data.columns)
        # if not_found_column:
        # not_found_column = ",".join(not_found_column)
        # print(not_found_column + " not found")
        # exit(0)

        # print(len(data))
        # NOTE: Selecting samples where selected columns mut have some value
        # TODO: Add following in test_file
        index = data[
            ~(
                pd.isna(data["REPOSITORY ID"])
                | pd.isna(data["STUDY TITLE"])
                | pd.isna(data["STUDY LINK"])
                | pd.isna(data["Run ID"])
            )
        ].index
        print(index)
        # TODO: Ask content team what would they like
        if len(index) < len(data):
            unselected_index = list(set(data.index) - set(index))
            unselected_index = np.sort(unselected_index)
            print("Please recheck following rows in your data")
            print(data.loc[unselected_index])
            print("Updating rest")
        data = data.loc[index]
        elo_wiki = pd.read_csv(
            "/home/devil/Documents/Tools/AMPData/fixed/elo_wiki.csv",
            usecols=["ELO", "WIKI"],
        )
        elo_wiki["ELO"] = elo_wiki["ELO"].apply(str.upper)
        # TODO: Merge the values where elo is
        tdata = data[~pd.isna(data["ELO"])]

        tdata["ELO"] = tdata["ELO"].apply(str.upper)
        print(tdata[pd.isna(tdata["STUDY LINK"])], "Anmol")
        print(elo_wiki[pd.isna(elo_wiki["ELO"])], "Kiran")
        data = data[pd.isna(data["ELO"])]
        tdata = tdata.merge(elo_wiki, on="ELO", how="inner")

        data = pd.concat([data, tdata])
        data.loc[pd.isna(data["WIKI"]), "WIKI"] = np.nan

        data = multi_value_columns_rows_allowed(data)

        # NOTE: only BioProject per line
        # NOTE: One sample/bioproject can be connected to multiple publications
        pubmed = data[["STUDY TITLE", "STUDY LINK"]].drop_duplicates()
        pubmed = pubmed.applymap(lambda val: str(val).upper())
        pubmed = pubmed.applymap(
            lambda values: [
                remove_multiple_spaces(value) for value in values.split("//")
            ]
        )
        pubmed_pair = []
        for _, row in pubmed.iterrows():
            for pair in zip(row["STUDY TITLE"], map(int, row["STUDY LINK"])):
                if pair not in pubmed_pair:
                    pubmed_pair.append(pair)
        pub_dict = update_pubmed(pubmed_pair)

        # NOTE: More than one disease can be associated with one sample
        disease = data.loc[~pd.isna(data["DISEASE"]), ["DISEASE", "DOID"]]
        # disease = data.loc[data["DISEASE"] != 'NAN', ["DISEASE", "DOID"]]
        disease = disease.applymap(lambda x: np.nan if x == "-" else x)
        disease = disease[~pd.isna(disease["DISEASE"])].drop_duplicates()

        disease = disease.applymap(lambda val: str(val).upper())
        disease = disease.applymap(
            lambda values: [
                remove_multiple_spaces(value) for value in values.split(",")
            ]
        )
        disease_pair = []

        def doid(val):
            try:
                return int(val)
            except:
                return None

        for _, row in disease.iterrows():
            for pair in zip(row["DISEASE"], map(doid, row["DOID"])):
                print(pair, "anmol")
                disease_pair.append(pair)
        # print(disease)
        disease_dict = upate_disease(disease_pair)

        # WARNING: Content team might mix sample to multiple body site.
        bodysite = data[["BODY SITE"]].drop_duplicates()
        bodysite = bodysite[~pd.isnull(bodysite["BODY SITE"])]
        bodysite = bodysite.applymap(lambda val: str(val).upper())
        bodysite = list(bodysite["BODY SITE"].values)
        body_site_dict = update_bodysite(bodysite)
        # Platform
        platform = data[
            ["PLATFORM", "TECHNOLOGY", "ASSAY TYPE", "TARGET AMPLICON"]
        ].drop_duplicates()
        plt_dict = update_platform(platform)

        # # WARNING: I hope Content team do not use multiple coordinates
        loc_diet = data[
            [
                "COUNTRY",
                "REGION",
                "CITYVILLAGE",
                "URBANZATION",
                "ETHNICITY",
                "ELO",
                "WIKI",
                "DIET",
            ]
        ].drop_duplicates()
        loc_diet_dict = update_loc_diet(loc_diet)
        print(loc_diet.columns)

        study_design = data[["STUDY DESIGN"]]
        study_design = study_design[
            ~pd.isna(study_design["STUDY DESIGN"])
        ].drop_duplicates()
        print(study_design)
        study_dict = update_study_design(study_design["STUDY DESIGN"].values)

        bioprojects = data[["REPOSITORY ID", "STUDY DESIGN"]].drop_duplicates()
        bioprojects_dict = update_bioproject(bioprojects, study_dict)

        # NOTE: Pushing samples in the table and connecting with other tables
        samples = data[
            [
                # # "STUDY DESIGN",
                "Run ID",
                # # "PARTICIPANT FEATURES",
                "AVERAGE SPOTLENGTH",
                "COLLECTION DATE",
                "LIBRARY LAYOUT",
                "LAT LON",  # TODO: Check where both field are there, else error
            ]
            + ["STUDY LINK"]
            + list(platform.columns)
            + ["BODY SITE"]
            + ["DISEASE"]
            + list(loc_diet.columns)
            + ["REPOSITORY ID"]
        ]
        # "TARGET AMPLICON",
        # "STUDY LINK", "PLATFORM", "TECHNOLOGY", "ASSAY TYPE"
        # ] + list(loc_diet.columns
        # ) + list(disease.columns
        # ) + list(assay.columns
        # )+list(amplicons.columns)
        # ].drop_duplicates("Run ID")
        samples.loc[:, ["LAT", "LON", "CAPITAL"]] = (
            samples["LAT LON"].apply(lan_lot).to_list()
        )
        del samples["LAT LON"]
        print(samples.head().values)
        # # NOTE:Considerting that each samples will have one samples collection date, one amplicon and etc
        # print(samples.head())
        print(loc_diet_dict)
        update_samples(
            samples,
            pub_dict,
            plt_dict,
            body_site_dict,
            disease_dict,
            loc_diet_dict,
            bioprojects_dict,
        )
