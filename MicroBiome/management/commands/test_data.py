from django.core.management.base import BaseCommand, CommandError
from MicroBiome import models
import pandas as pd
from os import path
import sys
import re
from geopy.geocoders import Nominatim


def remove_multiple_spaces(txt):
    """Removes multiple spaces from the text and strip spaces at the ends."""
    # print(txt)
    return re.sub(" +", " ", txt).strip()


def check_pubmed(pubmed_info):
    """Checking info in pubmed table."""
    for info in pubmed_info:
        if models.Pubmed.objects.filter(title__exact=info[0]):
            print(info, "Found")
        elif models.Pubmed.objects.filter(pubid__exact=info[1]):
            print(info, "Found")
        else:
            print(info, "Not found")


def check_disease(disease_info):
    """Checking info in pubmed table."""
    for info in disease_info:
        if models.Disease.objects.filter(disease__exact=info[0]):
            print(info, "Found")
        elif models.Disease.objects.filter(doid__exact=info[1]):
            print(info, "Found")
        else:
            print(info, "Not found")


def check_platform(platform_info):
    """Checking info in pubmed table."""
    for info in platform_info:
        print(info)
        if models.Platform.objects.filter(
            platform__exact=info[0], technology__exact=info[1], assay__exact=info[2]
        ):
            print(info, "Found")

        else:
            print(info, "Not found")


def check_loc_diet(loc_diet_info):
    """TODO: Docstring for check_loc_diet.

    :loc_diet_info: TODO
    :returns: TODO

    """
    for info in loc_diet_info:
        print(type(info[3]))
        if models.LocEthDiet.objects.filter(
            country__exact=info[0],
            region__exact=info[1],
            urbanization__exact=info[2],
            elo__exact=info[3],
            cityvillage__exact=info[4],
            diets__exact=info[5],
            ethnicity__exact=info[6],
            lon__exact=info[7],
            lat__exact=info[8],
            capital__exact=info[9],
        ):
            print(f"{info} Found")
        else:
            print(f"{info} Not Found")
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


def check_bodysite(bodysites):
    """TODO: Docstring for check_bodysite.

    :bodysites: TODO
    :returns: TODO

    """
    for bodysite in bodysites:
        if models.BodySite.objects.filter(bodysite__exact=bodysite):
            print(bodysite, "Found")
        else:
            print(bodysite, "Not found")


def projects(project_lits):
    """TODO: Docstring for projects.

    :project_lits: TODO
    :returns: TODO

    """
    pass
    # TODO: Generate warding if exists
    # models.Project.


def other_param(arg1):
    """TODO: Docstring for other_param.

    :arg1: TODO
    :returns: TODO

    """
    # Check if it is not reported earlier or any closely replated words are in
    # any table which could be utilised as replacement
    #
    pass


# TODO: Request admin to contact data provider in case of conflict.
# Especially when it is related to IDs


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


def review_outcome(data):
    """TODO: Docstring for review_outcome.

    :data: TODO
    :returns: TODO

    """
    pass


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
        if not path.exists(infile):
            print("Given file path doesn't exist.")
            exit(0)
        if not path.isfile(infile):
            print("Give path is not a file. Exiting . . . .")
            exit(0)
        try:
            data = pd.read_csv(
                infile,
                usecols=[
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
            print(data)
            # data_type = data.dtypes
            # for col in data_type.index:
            #     if col in []:
            #         if data_type[col].type != np.int64:
            #             print("Expected integer, got mixed or text values")
            #     else:
            #         print("Expected string, got float or integers")
            pubmed = data[["STUDY TITLE", "STUDY LINK"]].drop_duplicates()

            # pubmed = pubmed.applymap(
            #     lambda values: [
            #         remove_multiple_spaces(value)
            #         for value in values.split("//")
            #     ]
            # )
            # pubmed_pair = []
            # for _, row in pubmed.iterrows():
            #     for pair in zip(row["STUDY TITLE"], row["STUDY LINK"]):
            #         pubmed_pair.append(pair)

            # print(len(pubmed_pair))
            # check_pubmed(pubmed_pair)

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
            # check_disease(disease_pair)

            bodysite = data[["BODY SITE"]].drop_duplicates()
            bodysite = bodysite[~pd.isnull(bodysite["BODY SITE"])].fillna("")
            bodysite = list(bodysite["BODY SITE"].values)
            # print(bodysite)
            # check_bodysite(bodysite)

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

            # check_platform(platform_info)

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
            check_loc_diet(loc_diet.values)

            # for _, row in data.iterrows():
            #     print(row)
        except:
            print("Given file is in not csv formatted or some colums doesn't exist")
            exit(0)
