Installation
#############

Software requirements:
Python 3.9 with following packages:
  - numpy
  - xarray (including dask, netCDF4 and bottleneck)
  - pyyaml

Use the provided file conda-env_NOCOS-MIZ.yml to install a suitable conda environment.

Running
############
1) Adjust the configuration file config_MIZcalc_default.yml or make a new one and provide its name inside MIZengine_NOCOS.py
2) source activate mizNOCOS
3) python3 MIZengine_NOCOS.py

Info
#############

We use variable names as defined by CMIP6/CMOR (https://clipc-services.ceda.ac.uk/dreq/u/MIPtable::SImon.html, from here: https://clipc-services.ceda.ac.uk/dreq/index/miptable.html) :
- siconc
- sithick
- sivol
- siitdconc
- siitdthick
- siage
- sisali
(See explanations in config_MIZcalc_default.yml)


