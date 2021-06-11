import pandas as pd
from pandas.tseries.offsets import MonthEnd, YearEnd


def to_date(date_str):
    """Conevrt date string to date.

    :date_str: TODO
    :returns: TODO

    """
    # TODO: Check whether month and year are provided
    date = None
    if "-" in date_str:
        try:
            date = pd.to_datetime(date_str, format="%d-%m-%Y")
        except:
            try:
                date = pd.to_datetime(date_str, format="%m-%Y") + MonthEnd(1)
            except:
                try:
                    date = pd.to_datetime(
                        date_str.split("-")[-1], format="%Y"
                    ) + YearEnd(1)
                except:
                    pass
        return date.date()
    if "/" in date_str:
        try:
            date = pd.to_datetime(date_str, format="%d/%m/%Y")
        except:
            try:
                date = pd.to_datetime(date_str, format="%m/%Y") + MonthEnd(1)
            except:
                try:
                    date = pd.to_datetime(
                        date_str.split("/")[-1], format="%Y"
                    ) + YearEnd(1)
                except:
                    pass
        return date.date()
    else:
        date = pd.to_datetime(date_str, format="%Y") + YearEnd(1)
        return date.date()
