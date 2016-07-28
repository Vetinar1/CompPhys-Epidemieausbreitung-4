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
	glob.step+=10
	
	
	# draw
	# First, prepare figure
	pyplot.clf()
	
	
	if glob.method == "RK4":
		#inf.infectRK4All(glob.step)
		pyplot.text(-12, 71, "Calculation method: RK4")
	elif glob.method == "Euler":
		#inf.infectEulerAll(glob.step)
		pyplot.text(-12, 71, "Calculation method: Euler")
	else:
		#inf.infectODEsolverAll(glob.step)
		pyplot.text(-12, 71, "Calculation method: ODE")
	
	# Second, prepare data
	grid_x, grid_y = numpy.mgrid[-13:44:500j, 34:72:500j]
	zgrid = scipy.interpolate.griddata( (glob.inputData["longitude"], glob.inputData["latitude"]), glob.inf[glob.step]/glob.population, (grid_x, grid_y), method="linear")
	# Third, draw data
	glob.cont = glob.m.contourf(grid_x, grid_y, zgrid, cmap="YlOrRd")
	# Fourth, draw map
	glob.m.drawcoastlines()
	# Fifth, draw cities
	
	for i in range(0, glob.cities.size):
		#print(glob.population[i])
		if glob.population[i] < 1000000:
			glob.m.plot(glob.inputData["longitude"][i], glob.inputData["latitude"][i], "r.")
		else:
			glob.m.plot(glob.inputData["longitude"][i], glob.inputData["latitude"][i], "b.")
	
	
	colorbar = glob.m.colorbar(glob.cont, location="right")
	pyplot.text(-12, 70, "Day: {}".format(glob.step))
	pyplot.text(-12, 69, "Total infected: {}".format(round(numpy.sum(glob.inf[glob.step]), 2)))
	pyplot.text(-12, 68, "Total infected (percent): {}".format(round(numpy.sum(glob.inf[glob.step])/numpy.sum(glob.population), 8)))
	pyplot.text(-12,67, glob.disease)
	pyplot.text(-12,66, glob.containment)

# Function that sets up map for first frame
def setupMap():
	# from http://matplotlib.org/basemap/users/geography.html
	# coordinates of berlin, map projection cyl for easy coordinate transformation
	#glob.cont_ax = pyplot.gca()
	#glob.m2 = Basemap(projection='cyl', llcrnrlat=34, llcrnrlon=-13,  urcrnrlat=72, urcrnrlon=44, anchor="NE", fix_aspect=False, resolution="c")
	
	#glob.map_ax = pyplot.axes([0, 0, ])#fig)
	#glob.map_ax.set_axis_bgcolor((0, 0, 0, 0))
	#pyplot.sca(glob.map_ax)
	
	glob.m = Basemap(projection='cyl', llcrnrlat=34, llcrnrlon=-13,  urcrnrlat=72, urcrnrlon=44, anchor="NE", fix_aspect=False, resolution="c")
	glob.m.drawcoastlines()	
	glob.m.plot(glob.inputData["longitude"], glob.inputData["latitude"], "r.")
	
	#pyplot.sca(glob.cont_ax)

