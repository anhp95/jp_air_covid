#%%
def extract_station_type(text):
    """ Convert station code to station type """
    """ Refer to https://tenbou.nies.go.jp/download/explain_measuring_station.html """
    
    code = int(str(text)[5:7])

    if code > 0 and code < 51:
        return 0
    elif code > 50 and code < 81:
        return 1
    return 2


# %%
