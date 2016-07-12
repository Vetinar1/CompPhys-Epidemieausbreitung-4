# Implements auxiliary functions

# Import shit
import numpy

# Function that filters out cities with over 200k inhabitants


#Prozdur zum Einlesen der Daten aus den csv-Dateien.
#Gibt ein Array mit dem jeweiligen Name der Stadt ('cities'), der Einwohnerzahl ('population'), dem Breitengrad ('latitude')
#und dem Längengrad ('longitude') aus <- In Subarrays
def readCities(source):
    read=numpy.loadtxt(source, skiprows=1, delimiter="," , dtype={'names': ('cities', 'population', 'latitude', 'longitude'), 'formats': ('a20', 'i4', 'f8', 'f8')})
    output=numpy.zeros(len(read),dtype={'names': ('cities', 'S', 'I', 'R', 'latitude', 'longitude'), 'formats': ('U20', 'i4','i4','i4', 'f8', 'f8')})
    names=read['cities']
    for i in range(0, len(names)):
        output['cities'][i]=names[i].decode('UTF-8')
    output['S']=read['population']    
    output['latitude']=read['latitude']
    output['longitude']=read['longitude']

    return output

def createNewTemp(source):
	# Read Cities
	cities = readCities(source)
	
	# Remove cities with more than 200k inhabitants
	for city in cities:
         print(city)
         print(city[1])
         if city[1] < 200000:
             numpy.delete(cities, city)
	
	# Write into new file
	numpy.savetxt("temp.csv", cities, fmt=["%.20s", "%.1i","%.1i","%.1i", "%-.2f", "%-.2f"], delimiter=",", newline="\n")
	
	return cities
