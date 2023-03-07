#%%
import pandas as pd
import geopandas as gpd

from shapely.geometry import Point

from const import *
from utils import *


class Station:
    def __init__(self, year):
        self.station_df = None
        self.year = year
        self.input_txt = f"../data/station/unzip/TM{self.year}0000.txt"

        self._rename_cols()
        self._extract_latlon()
        self._extract_station_type()

    def _rename_cols(self):
        """Translate and Rename and select cols"""

        df = pd.read_csv(self.input_txt, encoding="shift_jisx0213")
        cols = list(JP_EN_STATION_COLS.keys())
        selected_df = df[cols]
        self.station_df = selected_df.rename(columns=JP_EN_STATION_COLS)

    def _extract_latlon(self):
        """Extract lat lon cols from original files"""

        self.station_df["lat"] = (
            self.station_df["lat_deg"].astype(float)
            + self.station_df["lat_min"].astype(float) / 60
            + self.station_df["lat_sec"].astype(float) / (3600)
        )

        self.station_df["lon"] = (
            self.station_df["lon_deg"].astype(float)
            + self.station_df["lon_min"].astype(float) / 60
            + self.station_df["lon_sec"].astype(float) / (3600)
        )

        self.station_df.drop(
            ["lat_deg", "lat_min", "lat_sec", "lon_deg", "lon_min", "lon_sec"],
            axis=1,
            inplace=True,
        )

        self.station_df["coords"] = list(
            zip(self.station_df["lon"], self.station_df["lat"])
        )
        self.station_df["coords"] = self.station_df["coords"].apply(Point)
        self.station_df = gpd.GeoDataFrame(
            self.station_df, geometry="coords", crs=WORLD_SHP.crs
        )

    def _extract_station_type(self):
        """Extract station type from station code"""
        station_types = [
            extract_station_type(sc) for sc in self.station_df["station_code"].values
        ]
        self.station_df["station_type"] = station_types


# %%
