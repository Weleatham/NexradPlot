#########################################################################
# Script created by Bill Leatham in August and September of 2021. 
# This script plots Level 2 Radar data over an openstreet map for 
# a user defined area (default is the NWS BOX CWA). The user must
# have the radar data downloaded and have the program point to that
# directory. Can use the nexrad-AWS-download.py script to get the 
# data. This script will plot only a single panel image - reflectivity.
#########################################################################
# Importing some methods that are needed. 
#import numpy as np
import matplotlib.colors as colors 
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as feat
import pyart, io, pytz, os, requests
import numpy as np
import metcolors as cmap
import cartopy.io.img_tiles as cimgt
from urllib.request import urlopen, Request
from PIL import Image
from datetime import datetime
from shapely.geometry import Point, Polygon
#########################################################################
# This points to the directory where the Level 2 Radar files are located
filedir = '/Users/triforce/Nexrad/08-23-2021/'
# What directory would you like the images to be placed in?
outdir = filedir+'Output/'
# What variable do you want plotted? Options are:
# z = Reflectivity
# v = Base Velocity
# cc = Correlation Coefficient
# zdr = Differential Reflectivity
# kdp = Differential Phase
# sw = Spectrum Width
# Please select one of the options listed above - default is reflectivity
variable = 'z'
# Putting in the lat/lon upper right and lower left hand box where to display
# the radar data. 
min_lon = -69.5
max_lon = -74.0
min_lat = 40.8
max_lat = 44.0
# Here is where you can choose the degree slice level you want - will want 
# to see the VCP mode and degree angles available. Default is for KBOX at 
# 0.5 degrees which is the lowest sweep.
sweep = 0
# Giving the user the option to plot warnings or not. Default is yes. 
# Change to n if you do not want warnings plotted.
plot_warns = 'y'
# What WFO warnings you want plotted use the 3 letter ID. Default is BOX and 
# surrounding CWAs.
wfoids = ['ALY','BOX','GYX','OKX']
# Which warnings do you want plotted. Default is all convective warnings.
# SV = Severe, TO = Tornado, FF = Flash Flood, MA = Marine.
warnings = ['FF','SV','TO','MA']
# The zoom level for the open street map - may have to play around with this
# depending on box scale. The default is 8, which works well for BOX CWA.
osm_zoom = 8
# The transparency of the radar image being plotted. 0 being you won't see
# the radar image and 1 being you won't see the background behind the radar.
# Looked like 0.3 and 0.4 was the sweet spot on little testing.
transparency = 0.3
# Here is the local timezone (used for labeling the plot)
local_timezone = pytz.timezone("US/Eastern")
################# Should not have to make any edits below this ################
# This method grabs an openstreet to be used as the background for the radar 
# data. 
def image_spoof(self, tile): # this function pretends not to be a Python script
    url = self._image_url(tile) # get the url of the street map API
    req = Request(url) # start request
    req.add_header('User-agent','Anaconda 3') # add user agent to request
    fh = urlopen(req) 
    im_data = io.BytesIO(fh.read()) # get image
    fh.close() # close url
    img = Image.open(im_data) # open image with PIL
    img = img.convert(self.desired_tile_form) # set image format
    return img, self.tileextent(tile), 'lower' # reformat for cartopy
# Here is where the warning polygons are downloaded and added based on the
# the current radar time. From the IEM page.
def warning_polygons(time,wfos,warn):
# The base url from the IEM API to get the warnings for the time listed.
	url = "https://mesonet.agron.iastate.edu/geojson/sbw.geojson?ts="
	req = requests.get(url+time)
# A JSON file of all the warnings across the US based on the time given.
	dataset = req.json()['features']
	warn_dict = {}
# Looping through list of the warnings the user provided that they want plotted. 
# Then adding it to the blank dictionary provided as a key to be used later.
	for warnings in warn:
		warn_dict[warnings] = {}
# Looping through the list of variables from the features section of the dataset.
	for i in dataset:
# Parsing through a couple more keys in the dictionary of the dataset.
		wfoid = i['properties']['wfo']
		warntype = i['properties']['phenomena']
		geometry = i['geometry']
		warnid = i['id']
# Grabbing only the warnings for the WFOs that the user lists at the beginning of
# the file.
		for listed in wfos:
			if wfoid == listed:
				for warnings in warn:
# Parsing through the data to only plot the warnings that the user selected. This
# gets rid of any advisories or statments.
					if warntype == warnings:
# Adding the geometry of the polygon to a type of warning along with the warning
# id information.
						warn_dict[warntype][warnid] = geometry['coordinates'][0][0]
# Looping through the keys and values of the dictionary previously created.
	for keys,val in warn_dict.items():
# Looping through each warning type and the geometry points and putting it into a 
# format that creates a polygon.
		for key2,vals in val.items():
			pts = []
			lons, lats = [], []
			for lon, lat in vals:
				pt = Point(lon,lat)
				pts.append(pt)
				lons.append(pt.x)
				lats.append(pt.y)
			shp = Polygon(pts)
# Here is where we add the different convective warning types to the radar map. Please note the colors
# selected for the warnings are based off the values shown on the NWS page. All this is being plotted
# using cartopy.
			if keys == 'FF':
				ax.add_geometries([shp],crs=ccrs.PlateCarree(),ec='#66ff00',facecolor='none',linewidth=2)
			elif keys == 'TO':
				ax.add_geometries([shp],crs=ccrs.PlateCarree(),ec='red',facecolor='none',linewidth=3)
			elif keys == 'SV':
				ax.add_geometries([shp],crs=ccrs.PlateCarree(),ec='yellow',facecolor='none',linewidth=1.5)
			elif keys == 'MA':
				ax.add_geometries([shp],crs=ccrs.PlateCarree(),ec='cyan',facecolor='none',linewidth=1.5)
			else:
				continue
# User selecting what radar data is plotted. This is then used later for 
# the title/labels, colormaps chosen and levels used on the maps. 
def whats_plotted(var):
	if var == 'z':
		vari_name = 'reflectivity'
		levels = np.arange(-30,80,1)
		color = cmap.twip_z_clr
		cmap_levels = np.arange(-30,80,5)
	elif var == 'v':
# Please note the default velocity field is in m/s
# the conversion is done later in the program. The levels
# selected are for the data in kts.
		vari_name = 'velocity'
		levels = np.arange(-120,120,1)
		color = cmap.enhanced_bv_clr
		cmap_levels = np.arange(-120,120,5)
	elif var == 'cc':
		vari_name = 'cross_correlation_ratio'
		levels = np.arange(0.20,1.04,0.01)
		color = cmap.awips_cc_clr
		cmap_levels = np.arange(0.20,1.04,0.02)
	elif var == 'zdr':
		vari_name = 'differential_reflectivity'
		levels = np.arange(-4.0,8.0,0.25)
		color = cmap.awips_zdr_clr
		cmap_levels = np.arange(-4.0,8.0,1)
	elif var == 'kdp':
		vari_name = 'differential_phase'
		levels = np.arange(-3.0,8.0,0.25)
		color =  cmap.awips_kdp_clr
		cmap_levels = np.arange(-3.0,8.0,1)
	elif var == 'sw':
# Please note the default spectrum width field is in m/s
# the conversion is done later in the program. The levels
# selected are for the data in kts.
		vari_name = 'spectrum_width'
		levels = np.arange(0,40,1)
		color = cmap.miller_sw_clr
		cmap_levels = np.arange(0,40,2)
	else:
		print("Please use one of the options listed")
	return(vari_name,levels,color,cmap_levels)
# Grabbing the variable name, levels and colormap that will be generated for 
# the plot.
vari_name,clevs,color,cmap_levs = whats_plotted(variable)
# Looping through the directory where the radar files are located. 
for file in os.listdir(filedir):
# Only going through the files in the directory.
	if os.path.isfile(os.path.join(filedir,file)):
		filename = filedir+os.fsdecode(file)
# Skipping the MDM and extra files as the pyart method chokes on these
		if 'MDM' in file or 'V06.' in file or '.DS' in file:
			continue
		else:
			# Opening up the file with the pyart method. 
			radar = pyart.io.read(filename)
			# A few variables for the title of the plot. 
			# The name of the radar site.
			radar_name = radar.metadata['instrument_name']
			# The VCP the radar is in.
			vcp_mode = radar.metadata['vcp_pattern']
			# This section here deals with if the user selects either velocity or 
			# spectrum width. Since the data is in m/s conversion is done so it can
			# be viewed in kts.
			if vari_name == 'velocity':
			# Changing the variable name used later on.
				vari_name = 'Base Velocity'
			# Making a copy of all the velocity data field and storing it
				vel_field = radar.fields['velocity']['data'].copy()
			# Multiplying the entire array by 1.94384 to convert it to kts.
				vel_in_kts = vel_field * 1.94384
			# Making the dictory of the dataset.
				var_dict = {'data':vel_in_kts,
					'units':'kts',
					'standard_name': 'Base Velocity',
					'long_name': 'Base Velocity',
					'_FillValue': vel_in_kts.fill_value
				}
			# Adding the newly created field to the radar data.
				radar.add_field('Base Velocity',var_dict, replace_existing=False)
			elif vari_name == 'spectrum_width':
			# Follows same steps as the velocity data above, but this time with
			# spectrum width.
				vari_name = 'Spectrum Width'
				sw_field = radar.fields['spectrum_width']['data'].copy()
				sw_in_kts = sw_field * 1.94384
				var_dict = {'data':sw_in_kts,
					'units':'kts',
					'standard_name': 'Spectrum Width',
					'long_name': 'Spectrum Width',
					'valid_max': 40.0,
					'valid_min': 0.0,
					'_FillValue':sw_in_kts.fill_value
				}
				radar.add_field('Spectrum Width',var_dict,replace_existing=False)
			# The variable name being plotted.
			name = radar.fields[vari_name]['long_name']
			# The units of the variable that is beingn plotted.
			var_units = radar.fields[vari_name]['units']
			# The degree slice being plotted. 
			degree_slice = str(round(radar.fixed_angle['data'][sweep],1))
			# Generating the timestamp to be displayed on the title. 
			# First removing the text that is attached to the time in UTC. 
			timestamp = radar.time['units'].replace('seconds since ','')
			# Converting the time to a datetime object.
			datetimeobj = datetime.strptime(timestamp,'%Y-%m-%dT%H:%M:%SZ')
			# Making the datetime object into a timezone.
			local_datetime = datetimeobj.replace(tzinfo=pytz.utc)
			#iem_stamp = local_datetime.strftime('%Y-%m-%dT%H:%M')
			# Converting the datetime object from UTC to the local timezone the user specifies above.
			# The second variable is for the title in the image and the first is for the filename, but
			# is in UTC.
			file_timestamp = local_datetime.strftime('%Y-%m-%d-%H%MZ')
			local_timestamp = local_datetime.astimezone(local_timezone).strftime('%b %d %Y %I:%M %p')
			# Graphing the radar data with the RadarMapDisplay method - plotted later on the
			# plot_ppi_map method. 
			display = pyart.graph.RadarMapDisplay(radar)
			# Grabbing the open street map to be loaded by cartopy later. 
			cimgt.OSM.get_image = image_spoof # reformat web request for street map spoofing
			osm_img = cimgt.OSM() # spoofed, downloaded street map
			# Making the figure x, y for size
			fig = plt.figure(figsize=(10, 8))
			# Adding the openstreet map as an axis to the plot
			ax = plt.axes(projection=osm_img.crs)
			# Sets the extent-max/min lon/lat box that the data will be displayed.
			# Defined by the user above.
			ax.set_extent([min_lon,max_lon,min_lat,max_lat])
			# This puts in a high resolution state boundary map on the plot.
			ax.add_feature(feat.STATES.with_scale('10m'))
			# This adds a high resolution coastline boundary to the plot.
			ax.add_feature(feat.COASTLINE)
			# This adds the street map layer to the background with a zoom level specified 
			# above. The default 8 worked well for a larger view of the NWS BOX CWA. 
			ax.add_image(osm_img, osm_zoom, interpolation='spline36')
			# Normalizing the colorbar scale by the number of levels in the cmap file from metcolors.py
			norm = colors.BoundaryNorm(clevs, color.N-1)
			# Adding in the warning polygons from IEM. 
			if plot_warns == 'y':
				warning_polygons(timestamp,wfoids,warnings)
			else:
				continue
			# Displaying the lowest slice of reflectivity data. Uses an alpha to set transparency so one can see the 
			# background map. Embelish gets rid of the low resolution coastline added by the plot_ppi_map method. 
			display.plot_ppi_map(vari_name, sweep=sweep, norm=norm, cmap=color, alpha=transparency, embelish=False,\
				title=radar_name+' '+degree_slice+' Degree '+name+'\n'+local_timestamp,\
				colorbar_label=vari_name+' ('+var_units+')',ticks=cmap_levs)
			# Saving the figure
			fig.tight_layout()
			fig.savefig(outdir+radar_name+'_'+degree_slice+'_'+name+'_'+file_timestamp+'.png')
			plt.close(fig)
print("The program has finished!")