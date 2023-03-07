#%%
import os
import glob
import geopandas as gpd

DATA_DIR = "../data"
LIST_STATION_CSV = glob.glob(os.path.join(DATA_DIR, "station", "unzip", "*.txt"))

JP_EN_STATION_COLS = {
    "国環研局番": "station_code",			
    "緯度_度":"lat_deg",
    "緯度_分":"lat_min",
    "緯度_秒":"lat_sec",
    "経度_度":"lon_deg",
    "経度_分":"lon_min",
    "経度_秒":"lon_sec",
    "市区町村コード":"city_code",
    "標高(m)":"elevation"
}

WORLD_SHP = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

# %%
