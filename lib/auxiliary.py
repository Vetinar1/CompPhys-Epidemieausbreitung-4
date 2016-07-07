# Implements auxiliary functions

# Import shit
import numpy

# Function that filters out cities with over 200k inhabitants


#Prozdur zum Einlesen der Daten aus den csv-Dateien.
#Gibt ein Array mit dem jeweiligen Name der Stadt ('cities'), der Einwohnerzahl ('population'), dem Breitengrad ('latitude')
#und dem Längengrad ('longitude') aus <- In Subarrays
def readCities(source):
	return numpy.loadtxt(source, skiprows=1, delimiter="," , dtype={'names': ('cities', 'population', 'latitude', 'longitude'), 'formats': ('S20', 'i4', 'f8', 'f8')})

def createNewTemp(source):
	# Read Cities
	global cities
	cities = readCities(source)
	
	# Remove cities with more than 200k inhabitants
	for city in cities:
		if city[1] < 200000:
			numpy.delete(cities, city)
	
	# Write into new file
	numpy.savetxt("temp.csv", cities, fmt=["%.20s", "%.1i", "%-.2f", "%-.2f"], delimiter=",", newline="\n")
