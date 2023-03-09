#%%

import pandas as pd

from const import *


def extract_station_type(text):
    """Convert station code to station type"""
    """ Refer to https://tenbou.nies.go.jp/download/explain_measuring_station.html """

    code = int(str(text)[5:7])

    if code > 0 and code < 51:
        return 0
    elif code > 50 and code < 81:
        return 1
    return 2


def read_multi_stations(list_txt):
    """Load multiple station txt files"""

    list_df = []
    for txt in list_txt:
        df = pd.read_csv(txt, encoding="shift_jisx0213")
        list_df.append(df)

    return pd.concat(list_df, ignore_index=True).rename(columns=JP_EN_MEASURE_COLS)

def load_annual_measure(year):
    data_dir = f"../data/measures/unzip/{year}/"

    

# %%
