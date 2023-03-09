#%%
import pandas as pd
import geopandas as gpd
import glob

from shapely.geometry import Point

from const import *
from utils import *


class StationLocation:
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


class MAAirQuality:
    pollutant_vars = [
        "CH4",
        "CO",
        "NMHC",
        "NO",
        "NO2",
        "NOX ",
        "OX  ",
        "PM25",
        "SO2 ",
    ]
    weather_vars = [""]

    def __init__(self, name, year) -> None:
        self.name = name
        self.year = f"{year}"

        self.jcode = []

        self._extract_jcode()
        self._load_annual_measures()
        self._extract_aq()

    def _extract_jcode(self):

        jcode_col = "JCODE"
        gdf_bound = gpd.read_file(os.path.join(MA_ATTR_DIR, f"{self.name}.shp"))
        self.jcode = [str(code) for code in gdf_bound[jcode_col].values if code]

    def _load_annual_measures(self):
        annual_files = []
        list_df = []
        # list all annual txt files
        annual_dir = os.path.join(AIR_DIR, self.year, "*")
        list_pref_dir = glob.glob(annual_dir)
        for pref_dir in list_pref_dir:
            annual_files += glob.glob(os.path.join(pref_dir, self.year, "*.txt"))

        # read all annual txt files
        for txt in annual_files:
            df = pd.read_csv(txt, encoding="shift_jisx0213")
            list_df.append(df)

        annual_df = pd.concat(list_df, ignore_index=True).rename(
            columns=JP_EN_MEASURE_COLS
        )
        # extract full mun_code
        annual_df["mun_code"] = [
            f"{str(sc)[0:2]}{mc}" if len(str(sc)) > 7 else f"0{str(sc)[0]}{mc}"
            for sc, mc in zip(
                annual_df["station_code"].values, annual_df["mun_code"].values
            )
        ]
        self.annual_df = annual_df

    def _extract_aq(self):

        self.aq = self.annual_df.loc[self.annual_df["mun_code"].isin(self.jcode)]

    def _preprocess_aq(self):
        # filter nodata
        # daily agg
        pass

    def _extract_weather(self):
        pass


# %%
