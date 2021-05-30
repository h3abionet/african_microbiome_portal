#!/usr/bin/env python
from .models import Project
import click
import pandas as pd


@click.command()
@click.option(
    "-inf",
    help="Input table in csv format",
    type=str,
    default=None,
    show_default=True,
)
def run(inf):
    if not inf:
        exit("Input file not given")
    df = pd.read_csv(inf)
    predef_names = set(
        [
            "REPOSITORY ID",
            "STUDY TITLE",
            "STUDY LINK",
            "ASSAY TYPE",
            "TECHNOLOGY",
            "COUNTRY",
            "DISEASE",
            "STUDY DESIGN",
            "BODY SITE",
            "PLATFORM",
            "PARTICIPANT FEATURES",
            "LIBRARY LAYOUT",
            "LON LAT",
            "SAMPLE TYPE",
            "COLLECTION DATE",
            "ETHNICITY",
            "URBANZATION",
            "REGION",
            "CITY",
            "TARGET AMPLICON",
            "DIET",
            "SAMPLE NUMBER",
        ]
    )
    if len(predef_names - set(df.columns)):
        print(
            predef_names - set(df.columns),
            "are not table columns names in gven table",
        )
        exit("Exiting.....")
    for _, row in df.iterrows():
        print(row)
        continue
        #  print(row['repository'])
        created = Project.objects.get_or_create(
            repository_id=row["REPOSITORY_ID"],  # max length was 11
            study_title=row["STUDY_TITLE"],
            study_link=row["STUDY_LINK"],
            assay_type=row["ASSAY_TYPE"],
            technology=row["TECHNOLOGY"],
            country=row["COUNTRY"],
            disease=row["DISEASE"],
            study_design=row["STUDY DESIGN"],
            body_site=row["BODY SITE"],
            platform=row["PLATFORM"],
            participant_features=row["PARTICIPANT FEATURES"],
            library_layout=row["LIBRARY LAYOUT"],
            lon_lat=row["LON LAT"],
            sample_type=row["SAMPLE TYPE"],
            collection_date=row["COLLECTION DATE"],
            ethnicity=row["ETHNICITY"],
            urbanzation=row["URBANZATION"],
            region=row["REGION"],
            city=row["CITY"],
            target_amplicon=row["TARGET AMPLICON"],
            diet=row["DIET"],
            sample_count=row["SAMPLE NUMBER"],
        )


if __name__ == "__main__":
    run()
