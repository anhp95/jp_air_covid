#%%
import os
import glob
import geopandas as gpd

DATA_DIR = "../data"
LIST_STATION_CSV = glob.glob(os.path.join(DATA_DIR, "station", "unzip", "*.txt"))

JP_EN_STATION_COLS = {
    "国環研局番": "station_code",
    "緯度_度": "lat_deg",
    "緯度_分": "lat_min",
    "緯度_秒": "lat_sec",
    "経度_度": "lon_deg",
    "経度_分": "lon_min",
    "経度_秒": "lon_sec",
    "市区町村コード": "city_code",
    "標高(m)": "elevation",
}

JP_EN_MEASURE_COLS = {
    "測定年度": "year",
    "測定局コード": "station_code",
    "市町村コード": "mun_code",
    "測定項目コード": "var",
    "測定単位コード": "unit",
    "測定月": "month",
    "測定日": "date",
}


LIST_POLLUTANTS = [
    "CH4",
    "CO",
    "NMHC",
    "NO",
    "NO2",
    "NOX",
    "OX",
    "PM25",
    "SO2",
    "SPM",
    "SPMB",
    "THC",
]

COL_JCODE = "JCODE"
COL_MUN_CODE = "mun_code"
COL_STATION_CODE = "station_code"
COL_VAR = "var"

MA_ATTR_DIR = "D:\SHP\jp_mma\shp_attr"

AIR_DIR = os.path.join(DATA_DIR, "measures/unzip")

WORLD_SHP = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

# %%
