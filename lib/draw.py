# Implements auxiliary functions

import numpy
import scipy
import scipy.interpolate
import matplotlib.pyplot as pyplot
from mpl_toolkits.basemap import Basemap
import lib.globals as glob
import lib.infection as inf
import lib.travel as travel

# Function that draws each frame
def update(bla):
	# increase steap count
	glob.step+=1
	
	# Move simulation forward by 1 day
	travel.travelLandAll(glob.step)
	travel.travelAirAll(glob.step)
	inf.infectRK4All(glob.step)
	
	# draw
	# First, prepare figure
	pyplot.clf()
	# Second, prepare data
	grid_x, grid_y = numpy.mgrid[-13:44:1000j, 34:72:1000j]
	zgrid = scipy.interpolate.griddata( (glob.inputData["longitude"], glob.inputData["latitude"]), glob.inf[glob.step]/glob.population, (grid_x, grid_y), method="linear")
	# Third, draw data
	glob.cont = glob.m.contourf(grid_x, grid_y, zgrid, cmap="YlOrRd")
	# Fourth, draw map
	glob.m.drawcoastlines()
	# Fifth, draw cities
	for i in range(0, glob.cities.size):
		print(glob.population[i])
		if glob.population[i] < 1000000:
			glob.m.plot(glob.inputData["longitude"][i], glob.inputData["latitude"][i], "r.")
		else:
			glob.m.plot(glob.inputData["longitude"][i], glob.inputData["latitude"][i], "b.")
	
	
	colorbar = glob.m.colorbar(glob.cont, location="right")
	pyplot.text(0, 70, glob.step)
	

# Function that sets up map for first frame
def setupMap():
	# from http://matplotlib.org/basemap/users/geography.html
	# coordinates of berlin, map projection cyl for easy coordinate transformation
	#def_ax = pyplot.gca()
	#def_ax.set_axis_bgcolor((0, 0, 0, 0))
	glob.m = Basemap(projection='cyl', llcrnrlat=34, llcrnrlon=-13,  urcrnrlat=72, urcrnrlon=44, anchor="NE", fix_aspect=False, resolution="c")
	glob.m.drawcoastlines()
	
	glob.m.plot(glob.inputData["longitude"], glob.inputData["latitude"], "r.")
	
	
	
'''
def draw():
	grid_x, grid_y = numpy.mgrid[-13:44:1000j, 34:72:1000j]
	zgrid = scipy.interpolate.griddata( (glob.inputData["longitude"], glob.inputData["latitude"]), glob.inf[-1], (grid_x, grid_y), method="linear")
	glob.m.contourf(grid_x, grid_y, zgrid, alpha=0.5)
	#new_ax = pyplot.axes([0, 0, 1, 1])#[-13, 34, 44+13, 72-34])
	#new_ax.set_axis_bgcolor((0, 0, 0, 0))
	#pyplot.show()

'''
