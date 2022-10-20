import numpy as np
import netCDF4 as nc4
import time       

# User provides the eruption parameters below

# Project name
proj='VolRes-RE'

# model name
model='modTBD'

# wavelength bands in SW and LW, wl1 and wl2 specify the lower and upper bound of each band, respectively
# wavelengths here in unit of micron (10**-6 m)
# dummy values included here so scripts run without modification
wl1_sw=[0.1, 0.3, 0.55, 0.75, 1.0, 2.0, 5.0]
wl2_sw=[0.3, 0.55, 0.75, 1.0, 2.0, 5.0, 8.0]
wl1_lw=[2.5, 4.0, 7.0, 10.3, 20]
wl2_lw=[4.0, 7.0, 10.3, 20, 30]

# latitude array
# dummy values inlcuded here so scripts run without modification
lat=[-80, -70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80]


# -----------------------------------------------------------------------------
# No further editing required below this point



nlat= np.shape(lat)[0]
nsw=np.shape(wl1_sw)[0]
nlw=np.shape(wl1_lw)[0]

# altitude
z=np.arange(5,40,0.5)
nz=np.shape(z)[0]

# save netcdf file
filename = proj + '_' + model + '_gridfile.nc'

nc = nc4.Dataset(filename, clobber=True, mode='w' )
nc.createDimension('altitude', nz)
nc.createDimension('latitude', nlat)
nc.createDimension('solar_bands', nsw)
nc.createDimension('terrestrial_bands',nlw)

nc.setncattr('title','Gridfile model=' + model + ' for use in the Easy Volcanic Aerosol (EVA) forcing generator')
nc.setncattr('history','Created ' + time.ctime(time.time()) )

# Create variables and set attributes:

nc_z = nc.createVariable('altitude', 'f8', 'altitude')                                        
nc_z.setncattr('units', 'km')

nc_lat = nc.createVariable('latitude', 'f8', 'latitude')
nc_lat.setncattr('units', 'degrees north')

nc_wl1_sun = nc.createVariable('wl1_sun', 'f8', 'solar_bands')
nc_wl1_sun.setncattr('units', 'lower boundary of wavelength of solar band in um')

nc_wl2_sun = nc.createVariable('wl2_sun', 'f8', 'solar_bands')
nc_wl2_sun.setncattr('units', 'upper boundary of wavelength of solar band in um')

nc_wl1_earth = nc.createVariable('wl1_earth', 'f8', 'terrestrial_bands')
nc_wl1_earth.setncattr('units', 'lower boundary of wavelength of terrestrial band in um')

nc_wl2_earth = nc.createVariable('wl2_earth', 'f8', 'terrestrial_bands')
nc_wl2_earth.setncattr('units', 'upper boundary of wavelength of terrestrial band in um')

# Write data to file:
nc_z[:]         = z
nc_lat[:]       = lat  
nc_wl1_sun[:]   = wl1_sw 
nc_wl2_sun[:]   = wl2_sw
nc_wl1_earth[:] = wl1_lw
nc_wl2_earth[:] = wl2_lw

nc.close()
    
