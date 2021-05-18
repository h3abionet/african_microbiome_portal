import pandas as pd


"""
Code in this file convert table values to sql aceptable values.

"""


def loc_correct(row):
    """
    Replaces string missing value with 'nan' and numerical values to None for
    location related informtion
    """
    for k in row.index:
        #  print(k, "Anmol Kiran")
        if pd.isna(row[k]):
            if k in ["LON", "LAT"]:
                row[k] = None
            else:
                row[k] = "nan"
    return row


def platform_correct(row):
    """Fixes missings platform related issue"""
    for k in row.index:
        if pd.isna(row[k]):
            row[k] = "nan"
    return row


def assay_correct(row):
    """Fixes missings platform related issue"""
    for k in row.index:
        if pd.isna(row[k]):
            row[k] = "nan"

    return row


def amplicon_correct(row):
    """Fixes missings amplicon related issue"""
    for k in row.index:
        if pd.isna(row[k]):
            row[k] = "nan"
    return row

def bodysite_correct(row):
    """Fixes missings bodysite related issue"""
    for k in row.index:
        if pd.isna(row[k]):
            row[k] = "nan"
    return row
