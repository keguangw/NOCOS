
def save_toNetcdf(mizdata,icedata,configs):

    import numpy as np
    import datetime
    import os
    
    # MIZmethod as string
    mizmethod=[i for i in configs['MIZmethod'] if configs['MIZmethod'][i]==True][0]
    
    # Create the output filename
    if configs['output']['filename_automatic'] == True:
        outfile = configs['output']['output_folder']+'/MIZ-' + mizmethod[1:] +'_' +  \
                  os.path.basename(configs['ice_filename']).replace('*','XXX').replace('?','X')
    else:
        outfile = configs['output']['output_folder'] + '/' + configs['output']['filename']
    
    # Make an empty dataset with basic coordinates for the netcdf file, copied from the icedata-file
    timespace_coords=[configs["coordinates"]["lon_name"], configs["coordinates"]["lat_name"], configs["coordinates"]["time_name"]]
    mizds=icedata[timespace_coords] # Create an "empty" DataSet with same time and space dimentions as in icedata

    # Add the MIZ variable with dimensions, attributes and data from mizdata
    miz_dims = (icedata.siconc.dims[0],icedata.siconc.dims[1],icedata.siconc.dims[2]) # (time, y, x)
    mizds["MIZ"] = (miz_dims, mizdata)
    miz_attrs={'long_name': mizmethod[1:] + ' Marginal ice zone',
                'units':'[]'}
    mizds.MIZ.attrs=miz_attrs

    ## Try to correct the attribute 'coordinates' of the MIZ variable in netcdf. For DMI data, xarray's automatic does it wrongly. But this doesn't work:
    #miz_coords=configs["coordinates"]["lon_name"] +' '+ configs["coordinates"]["lat_name"] +' shipclass '+ configs["coordinates"]["time_name"]
    #mizds["MIZ"] = (miz_dims, mizfinal, {'coordinates':miz_coords})
    #mizds.MIZ.encoding["coordinates"]=miz_coords
    
    # Set global attributes of the netcdf file
    mizds.attrs={
    'title':configs['output']['title'],
    'histroy':'Created by MIZengine_NOCOS.py on '+datetime.datetime.today().strftime("%Y-%m-%d"),
    'description':'Used MIZ calculation method: '+mizmethod+'; number of ice categories: '+str(configs['coordinates']['ncat']),
    'institution':"Norwegian Meteorological Institutes, MetNO",
    'references':'https://doi.org/10.5194/tc-17-4487-2023'
    }
    
    # Write netcdf file
    mizds.to_netcdf(outfile, unlimited_dims=configs["coordinates"]["time_name"], encoding={'MIZ':{'_FillValue':np.nan},'time':{"dtype": "double", 'units': "days since 1970-01-01 00:00:00"}})
    print("MIZ output written to: "+outfile)
