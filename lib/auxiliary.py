# Implements auxiliary functions

# Import shit
import numpy as np

# Function that filters out cities with over 200k inhabitants


#Prozdur zum Einlesen der Daten aus den csv-Dateien.
#Gibt ein Array mit dem jeweiligen Name der Stadt ('cities'), der Einwohnerzahl ('population'), dem Breitengrad ('latitude')
#und dem Längengrad ('longitude') aus <- In Subarrays
def readCities(filename):
       return np.loadtxt(filename, skiprows=1, delimiter="," ,\
                       dtype={'names': ('cities', 'population', 'latitude', 'longitude'),\
                              'formats': ('S20', 'i4', 'f8', 'f8')})
    
