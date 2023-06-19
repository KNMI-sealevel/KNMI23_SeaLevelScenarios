# KNMI23 functions

# Paths
root = '/Users/dewilebars/Projects/'
slproj_dir = f'{root}/Project_ProbSLR/SLProj/'
finger_dir = f'{root}/Project_ProbSLR/Data_Proj/Data_AR5/Fingerprints/'

# Import libraries
import xarray as xr

import sys
sys.path.append(f'{slproj_dir}code')

import func_misc as misc

# Define functions
def read_constant_fp(method, lat, lon):

    if method == 'AR5':
        f_gic = xr.open_dataset(finger_dir+'Relative_GLACIERS_reg.nc', \
                                     decode_times=False)
        F_gic = misc.finger1D(lat, lon, f_gic.latitude, f_gic.longitude, 
                              f_gic.RSL)[-1].values.item()/100

        f_ic        = xr.open_dataset(finger_dir+'Relative_icesheets_reg.nc')
        lat_ic      = f_ic.latitude #tofloat?
        lon_ic      = f_ic.longitude
        F_gsmb      = misc.finger1D(lat, lon, lat_ic, lon_ic, 
                                    f_ic.SMB_GRE).values.item()/100
        F_asmb      = misc.finger1D(lat, lon, lat_ic, lon_ic, 
                                    f_ic.SMB_ANT).values.item()/100
        F_gdyn      = misc.finger1D(lat, lon, lat_ic, lon_ic, 
                                    f_ic.DYN_GRE).values.item()/100
        F_adyn      = misc.finger1D(lat, lon, lat_ic, lon_ic, 
                                    f_ic.DYN_ANT).values.item()/100
        f_gw       = xr.open_dataset(finger_dir+'Relative_GROUNDWATER_reg.nc',
                                     decode_times=False)
        F_gw       = misc.finger1D(lat, lon, f_gw.latitude, f_gw.longitude, 
                                   f_gw.GROUND)[-1].values.item()/100
    
    else:
        print('Method not supported')
    
    fingerprints = {'GIC': F_gic, 'GSMB': F_gsmb, 'ASMB': F_asmb, 
                    'GDYN': F_gdyn, 'ADYN': F_adyn, 'GW': F_gw}
    
    return fingerprints

def new_ref_period(da):
    '''Change the reference period coming out of the sea level projection code 
    1986-2005 to that of the AR6 and KNMI'23 projections'''
    
    da_rp2 = da - da.sel(time=slice(1995,2015),percentiles='50').mean(dim='time')
    
    return da_rp2