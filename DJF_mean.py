# DJF mean yearly

import xarray as xr
import numpy as np
import pandas as pd


def DJF_mean(data,strtyr,endyr):
    
    djf  = data.where(data['time.season'] == 'DJF')
    djf_mean = djf.rolling(min_periods=3, center=True, time=3).mean()
    djf_groupby_mean = djf_mean.groupby('time.year').mean('time',keep_attrs=True)
    djf_sel = djf_groupby_mean.sel(year=slice(strtyr,endyr)).rename({'year': 'time'})
        
    return djf_sel
