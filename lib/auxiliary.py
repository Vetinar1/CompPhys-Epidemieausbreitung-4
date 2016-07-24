# Implements auxiliary functions

# Import shit
import numpy
import scipy.interpolate
import matplotlib.pyplot as pyplot
from mpl_toolkits.basemap import Basemap
import lib.globals as glob

# Function that filters out cities with over 200k inhabitants


#Prozdur zum Einlesen der Daten aus den csv-Dateien.
#Gibt ein Array mit dem jeweiligen Name der Stadt ('cities'), der Anzahl gesunder Leute (hier noch gleich der Einwohnerzahl) ('S'), der Anzahl kranker Leute (hier noch 0) ('I'), der Anzahl immuner Leute (hier noch 0) ('R'),  dem Breitengrad ('latitude') und dem Längengrad ('longitude') aus <- In Subarrays
def readCities(source):
	#read from file:
    read=numpy.loadtxt(source, skiprows=1, delimiter="," , dtype={'names': ('cities', 'population', 'latitude', 'longitude'), 'formats': ('a20', 'i4', 'f8', 'f8')})
    
    # Remove cities with more than 200k inhabitants
    for city in read:
    	if city['population'] < 200000:
    		numpy.delete(read, city)
     
	#create an new array filled with zeros with the additional field for 'I' and 'R'
    output=numpy.zeros(len(read),dtype={'names': ('cities', 'population',  'latitude', 'longitude'), 'formats': ('U20', 'i4', 'f8', 'f8')})
	
	#decode Strings:
    names=read['cities']
    for i in range(0, len(names)):
        output['cities'][i]=names[i].decode('UTF-8')
		
	#fill the rest of the output-array with the datas read from the file:
    output['population']=read['population']    
    output['latitude']=read['latitude']
    output['longitude']=read['longitude']

    return output


def setupMap():
	# from http://matplotlib.org/basemap/users/geography.html
	# coordinates of berlin, map projection cyl for easy coordinate transformation
	def_ax = pyplot.gca()
	#def_ax.set_autoscale_on(True)
	def_ax.set_axis_bgcolor((0, 0, 0, 0))
	glob.m = Basemap(projection='cyl', llcrnrlat=34, llcrnrlon=-13,  urcrnrlat=72, urcrnrlon=44, anchor="NE", fix_aspect=False)
	#glob.m.shadedrelief(scale=0.5)
	glob.m.drawcoastlines()
	
	glob.m.plot(glob.inputData["longitude"], glob.inputData["latitude"], "r.")
	#glob.ax = pyplot.axes([0, 0, 1, 1])#[-13, 34, 44+13, 72-34])
	#glob.ax.set_alpha(0.1)
	#return m
	#lon, lat = numpy.meshgrid(glob.inputData["longitude"], glob.inputData["latitude"])
	#print(lon.shape)
	#print(lat.shape)
	#blurb = numpy.random.rand(243)
	#print(blurb)
	#print(numpy.ma.getmask(blurb))
	#print(numpy.ma.getmask(lon))
	#print(numpy.ma.getmask(lat))
	
	
	#draw()
	#pyplot.show()

def draw():
	grid_x, grid_y = numpy.mgrid[-13:44:1000j, 34:72:1000j]
	zgrid = scipy.interpolate.griddata( (glob.inputData["longitude"], glob.inputData["latitude"]), glob.inf[-1], (grid_x, grid_y), method="linear")
	glob.m.contourf(grid_x, grid_y, zgrid, alpha=0.5)
	#new_ax = pyplot.axes([0, 0, 1, 1])#[-13, 34, 44+13, 72-34])
	#new_ax.set_axis_bgcolor((0, 0, 0, 0))
	#pyplot.show()

