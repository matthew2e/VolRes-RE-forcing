# Script for creating volcanic forcing files for the DCPP Volcanic Response Readiness Experiment (VolRes-RE)
# 
# This script will not run fully unless the EVA FORTRAN submodule is compiled. Compilation pointers can be found in the easy-volcanic-aerosol directory

# User steps
# 1. Compile EVA
# 2. Adapt variables in 'build_netcdf_gridfile.py' python script to your model (model name, latitude array and wavelengths)
# 3. Modify variable "model" below to the same model name as used in the 'build_netcdf_gridfile.py' script
# 4. Run this script
# 5. EVA forcing files will be created in the format of the CMIP6 historical volcanic forcing files. Users will need to interpolate these files to the vertical grid of their model.

model='modTBD'

python build_netcdf_gridfile.py
cp eva_namelist_VolRes-RE eva_namelist
sed -i 's/modX/'${model}'/g' eva_namelist
cp eva_namelist easy-volcanic-aerosol/

cd easy-volcanic-aerosol
./eva_build_sulfate_file
./eva_build_forcing_files_cmip6


