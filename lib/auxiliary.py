# Implements auxiliary functions

# Import shit
import numpy
import matplotlib.pyplot as pyplot
from mpl_toolkits.basemap import Basemap

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


def setupMap(inputData):
	# from http://matplotlib.org/basemap/users/geography.html
	# coordinates of berlin, map projection cyl for easy coordinate transformation
	m = Basemap(projection='cyl', llcrnrlat=34, llcrnrlon=-13,  urcrnrlat=72, urcrnrlon=44)#, fix_aspect=False)
	m.shadedrelief(scale=0.5)
	
	m.plot(inputData["longitude"], inputData["latitude"], "r.")
	pyplot.show()

def draw(inputData):
	pyplot.contourf(inputData["longitude"], inputData["latitude"], inf)
