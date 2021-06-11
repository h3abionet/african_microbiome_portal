from django.core.management.base import BaseCommand, CommandError
from MicroBiome import models
import pandas as pd
from os import path
import sys

import re
from geopy.geocoders import Nominatim


def remove_multiple_spaces(txt):
    """Removes multiple spaces from the text and strip spaces at the ends."""
    return re.sub(" +", " ", txt).strip()


def upate_disease(disease_info):
    """TODO: Docstring for disease.

    :arg1: TODO
    :returns: TODO

    """
    for i, info in enumerate(disease_info):
        print(i, info)
        try:
            models.Disease.objects.get_or_create(disease=info[0], doid=info[1])
        except:
            print("Please check for the value decripancies")


def update_bodysite(bodysites):
    """TODO: Docstring for check_bodysite.

    :bodysites: TODO
    :returns: TODO

    """
    for bodysite in bodysites:
        try:
            models.BodySite.objects.get_or_create(bodysite=bodysite)
        except:
            print("Please check for the value decripancies")


def update_platform(platform_info):
    """Checking info in pubmed table."""
    for info in platform_info:
        try:
            print(info)
            models.Platform.objects.get_or_create(
                platform=info[0], technology=info[1], assay=info[2]
            )

        except:
            print(f"Please check platform related information {info}")


def update_loc_diet(loc_diet_info):
    """TODO: Docstring for check_loc_diet.

    :loc_diet_info: TODO
    :returns: TODO

    """
    for info in loc_diet_info:
        try:
            models.LocEthDiet.objects.get_or_create(
                country=info[0],
                region=info[1],
                urbanization=info[2],
                elo=info[3],
                cityvillage=info[4],
                diets=info[5],
                ethnicity=info[6],
                lon=info[7],
                lat=info[8],
                capital=info[9],
            )
        except:
            print(f"Please check geo related information")
    # [
    #     "COUNTRY",
    #     "REGION",
    #     "URBANZATION",
    #     "ELO",
    #     "CITYVILLAGE",
    #     "DIET",
    #     "LAT LON",
    #     "ETHNICITY",
    # ]
    # pass


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
    return lan.strip(), lot.strip(), capital


def update_pubmed(pubmed_info):
    """TODO: Docstring for upload_pubmed.

    :pubmed_info: TODO
      :returns: TODO

    """
    for i, info in enumerate(pubmed_info):
        print(i, info)
        try:
            models.Pubmed.objects.get_or_create(title=info[0], pubid=info[1])
        except:
            print("Please check for the value decripancies")


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
        try:
            data = pd.read_csv(
                infile,
                usecols=[
                    "REPOSITORY ID",
                    "REPOSITORY LINK",
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
                    "Sample ID",
                    "Sample Name",
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
                ],
            )
            data = data.applymap(lambda val: str(val).upper())
            pubmed = data[["STUDY TITLE", "STUDY LINK"]].drop_duplicates()

            pubmed = pubmed.applymap(
                lambda values: [
                    remove_multiple_spaces(value) for value in values.split("//")
                ]
            )
            pubmed_pair = []
            for _, row in pubmed.iterrows():
                for pair in zip(row["STUDY TITLE"], row["STUDY LINK"]):
                    if pair not in pubmed_pair:
                        pubmed_pair.append(pair)

            # update_pubmed(pubmed_pair)

            disease = data[["DISEASE", "DOID"]].drop_duplicates()
            disease = disease[~pd.isnull(disease["DISEASE"])].fillna("")

            disease = disease.applymap(
                lambda values: [
                    remove_multiple_spaces(value) for value in values.split("//")
                ]
            )
            disease_pair = []
            for _, row in disease.iterrows():
                for pair in zip(row["DISEASE"], row["DOID"]):
                    disease_pair.append(pair)
            # upate_disease(disease_pair)

            bodysite = data[["BODY SITE"]].drop_duplicates()
            bodysite = bodysite[~pd.isnull(bodysite["BODY SITE"])].fillna("")
            bodysite = list(bodysite["BODY SITE"].values)
            # update_bodysite(bodysite)

            # Platform
            platform = (
                data[["PLATFORM", "TECHNOLOGY", "ASSAY TYPE"]]
                .drop_duplicates()
                .fillna("")
            )

            platform = platform.applymap(
                lambda values: [
                    remove_multiple_spaces(value) for value in values.split("//")
                ]
            )
            platform_info = []
            for _, row in platform.iterrows():
                for triple in zip(
                    row["PLATFORM"], row["TECHNOLOGY"], row["ASSAY TYPE"]
                ):
                    platform_info.append(triple)

            # update_platform(platform_info)

            loc_diet = data[
                [
                    "COUNTRY",
                    "REGION",
                    "URBANZATION",
                    "ELO",
                    "CITYVILLAGE",
                    "DIET",
                    "LAT LON",
                    "ETHNICITY",
                ]
            ].drop_duplicates()
            # loc_diet.loc[:, ["LAN", "LOT"]] = loc_diet["LAT LON"].apply(lan_lot)
            loc_diet.loc[:, ["LAN", "LOT", "CAPITAL"]] = (
                loc_diet["LAT LON"].apply(lan_lot).to_list()
            )
            del loc_diet["LAT LON"]
            update_loc_diet(loc_diet.values)

            project_tab = None
            sample_tab = None
            disease_tab = None
            platform_tab = None
            geo_tab = None

        except:
            exit("File has some issue")
        print(infile)
