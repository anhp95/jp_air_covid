#%%
import pandas as pd


from utils import *
"""
Step 1: Preprocess statiosn
Step 2: Filter stations by cities
"""




def prep_stations(list_station_csv):
    for csv_file in list_station_csv:

        year_df = pd.read_csv(csv_file, encoding="shift_jisx0213")

        station_code = year_df.


def filter_stations_cities(prep_st_csv):
    pass