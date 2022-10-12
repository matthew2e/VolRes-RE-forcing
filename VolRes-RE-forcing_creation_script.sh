# Script for creating volcanic forcing files for the DCPP Volcanic Response Readiness Experiment (VolRes-RE)
# 
# This script will not run fully unless the EVA FORTRAN submodule is compiled. Compilation pointers can be found in the easy-volcanic-aerosol directory

# User steps
# 1. Compile EVA
# 2. Check the files in directory easy-volcanic-aerosol/gridfiles. Do you see a gridfile that matches your model, in terms of latitude resolution and wavelength bands? 
# 3a. If yes to 2:
#    modify variable 'model' below to match the full model name of the pre-existing gridfile, e.g., 'CanESM' or 'MIROC3.2_29'
#    modify variable 'proj' below to match the project identifier of the pre-existing gridfile, e.g., 'CMIP6' or 'CMIP'
# 3b. If no to 2:
#    Adapt variables in 'build_netcdf_gridfile.py' python script to your model (model name, latitude array and wavelengths)
#    Modify variable 'model' below to match what you have entered in 'build_netcdf_gridfile.py', and leave proj='VolRes-RE'
# 4. Run this script
# 5. EVA forcing files will be created in the format of the CMIP6 historical volcanic forcing files. Users will need to interpolate these files to the vertical grid of their model.

proj='VolRes-RE'
model='CanESM'

if [[ "$proj" == 'VolRes-RE' ]]; then
	echo 'building new gridfile'
     	python build_netcdf_gridfile.py
	cp ${proj}_${model}_gridfile.nc easy-volcanic-aerosol/gridfiles
fi

cp eva_namelist_VolRes-RE eva_namelist
sed -i 's/projX/'${proj}'/g' eva_namelist
sed -i 's/modX/'${model}'/g' eva_namelist
cp eva_namelist easy-volcanic-aerosol/

cd easy-volcanic-aerosol
./eva_build_sulfate_file
./eva_build_forcing_files_cmip6


