# Implements travel (auxiliary) functions

import numpy
import lib.globals as glob


	
 
def createLandConnections(inputData):
    # Initialize Land connections
    # First, create 2D array full of zeros; each row/column index n corresponds to one cities[n]
    landConnections = numpy.zeros((inputData.size, inputData.size))
    
    # Put a 1 in each field corresponding to dist < 500 km <= REWORD THIS
    for i in range(inputData.size):
        for j in range(inputData.size):
            # If distance between city and city2 < 500km, create connection
            # NOTE: Distance calculation according to http://www.kompf.de/gps/distcalc.html
            # -> dist = 6378.388 * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon2 - lon1))
            lat1=inputData[i][2]*numpy.pi/180
            lon1=inputData[i][3]*numpy.pi/180
            lat2=inputData[j][2]*numpy.pi/180
            lon2=inputData[j][3]*numpy.pi/180
            
            #print(dist)
            if i != j:
                dist=6378.388 * numpy.arccos(numpy.sin(lat1) * numpy.sin(lat2) + numpy.cos(lat1) * numpy.cos(lat2) * numpy.cos(lon2 - lon1))
                if dist < 500:
                    landConnections[i][j] = 1
                    
    return landConnections
	
	
def createAirConnections(inputData):
	# Initialize Land connections
	# First, create 2D array full of zeros; each row/column index n corresponds to one cities[n]
	airConnections = numpy.zeros((inputData.size, inputData.size))
	
	# 1 for each connection
	for i in range(inputData.size):
		# More than 1M inhabitants?
		if inputData[i][1] > 1000000:
			for j in range(inputData.size):
				# Also more than 1M inhabitants?
				if inputData[j][1] > 1000000 and i != j:
					airConnections[i][j] = 1
	return airConnections
 

def probabilities(connections,probability):
    #creates an 2d-array with the probabilities for traveling between two cities. The probabilitiy is higher to travel in big cities.
    probs=numpy.zeros((len(connections),len(connections)))
    for i in range(len(connections)):
        populationAllDestinations = numpy.sum(connections[i]*glob.population) #computes the sum of the population of all reachable cities via the given connection
        numberOfConnections = numpy.sum(connections[i])
        if numberOfConnections!=0:   # to avoid a division by zero. if the number of connections is zero, the probability stays zero, too
            for j in range(len(connections[i])):
                probs[i][j]=connections[i][j]*probability*glob.population[j]/populationAllDestinations
    return probs

	

def travelLand(citieIndex,actualPopulations):
    #computes all changes of the population of the citie with the given citieIndex because of the movement of travel via land
    departure = numpy.sum(glob.probabilitiesLand[citieIndex])*actualPopulations[citieIndex]
    entry = numpy.sum(actualPopulations*glob.probabilitiesLand[:,citieIndex])
    change=entry-departure    
    return actualPopulations[citieIndex]+change


def travelAir(citieIndex,actualPopulations):
    #computes all changes of the population of the citie with the given citieIndex because of the movement of travel via air
    departure = numpy.sum(glob.probabilitiesAir[citieIndex])*actualPopulations[citieIndex]
    entry = numpy.sum(actualPopulations*glob.probabilitiesAir[:,citieIndex])
    change=entry-departure    
    return actualPopulations[citieIndex]+change

 
 
def travelAll(f,actualPolulations):
    newPopulations=numpy.zeros(len(actualPolulations))
    for i in range(len(actualPolulations)):
        newPopulations[i]=f(i,actualPolulations)
    return newPopulations

	
def travelLandAll(step):
    glob.sus[step]=travelAll(travelLand,glob.sus[step-1])
    glob.inf[step]=travelAll(travelLand,glob.inf[step-1])
    glob.rec[step]=travelAll(travelLand,glob.rec[step-1])
    glob.dead[step]=glob.dead[step-1]
    return
    
	
def travelAirAll(step):
    glob.sus[step]=travelAll(travelAir,glob.sus[step])
    glob.inf[step]=travelAll(travelAir,glob.inf[step])
    glob.rec[step]=travelAll(travelAir,glob.rec[step])
    
    return
	
