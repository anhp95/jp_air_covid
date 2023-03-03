#%%
import os
import glob

DATA_DIR = "../data"
LIST_STATION_CSV = glob.glob(os.path.join(DATA_DIR, "station", "unzip", "*.txt"))

JP_EN_STATION_COLS = {
    "国環研局番": "station_code",
    
}

# %%
