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
        #compute the sum of the population of all reachable cities via the given connection:
        populationAllDestinations = numpy.sum(connections[i]*glob.population) 
        numberOfConnections = numpy.sum(connections[i])
        if numberOfConnections!=0:   # to avoid a division by zero. if the number of connections is zero, the probability stays zero, too
            for j in range(len(connections[i])):
                #probability is zero, when theres no connection (connection[i][j]=0)
                #the total probability will be splitted to the existing connection:
                probs[i][j]=connections[i][j]*probability*glob.population[j]/populationAllDestinations 
    return probs

	
#computes all changes of the population of the citie with the given citieIndex because of the movement of travel via land
def travelLand(citieIndex,actualPopulations,prob):
    departure = numpy.sum(prob[citieIndex])*actualPopulations[citieIndex]
    entry = numpy.sum(actualPopulations*prob[:,citieIndex])
    change=entry-departure    
    return actualPopulations[citieIndex]+change


#computes all changes of the population of the citie with the given citieIndex because of the movement of travel via air
def travelAir(citieIndex,actualPopulations,prob):	
    departure = numpy.sum(prob[citieIndex])*actualPopulations[citieIndex]
    entry = numpy.sum(actualPopulations*prob[:,citieIndex])
    change=entry-departure    
    return actualPopulations[citieIndex]+change
					

 
#compute travel for all cities, needs a function f (travelLand or travelAir), an array of all actual populations in the cities and the total probability for the given way of traveling 
def travelAll(f,actualPolulations,prob):
    newPopulations=numpy.zeros(len(actualPolulations))
    for i in range(len(actualPolulations)):
        newPopulations[i]=f(i,actualPolulations,prob)
    return newPopulations

#compute travel for all cities via land	
def travelLandAll(step):
    #the travel has to be computed for the groups arrays sus, inf, rec and dead:
    #travelLand is the first method to be called in one step of the SIR model. Therefore the input data is in the field [step-1]
    glob.sus[step]=travelAll(travelLand,glob.sus[step-1],glob.probabilitiesLand)
    glob.inf[step]=travelAll(travelLand,glob.inf[step-1],glob.probabilitiesLand*glob.ptInf) #probabilities multiplied with ptInf to implement a lower probability of traveling for infected people
    glob.rec[step]=travelAll(travelLand,glob.rec[step-1],glob.probabilitiesLand)
    glob.dead[step]=glob.dead[step-1] #dead people don't travel anymore, they stay the same from one to another step during traveling
    return
    
#compute travel for all cities via air
def travelAirAll(step):
    #the travel has to be computed for the groups arrays sus, inf and rec:
    #travelAir is called after travelLand. Therefore the input data is in the actual field [step]
    glob.sus[step]=travelAll(travelAir,glob.sus[step],glob.probabilitiesAir)
    glob.inf[step]=travelAll(travelAir,glob.inf[step],glob.probabilitiesAir*glob.ptInf)
    glob.rec[step]=travelAll(travelAir,glob.rec[step],glob.probabilitiesAir)    
    return
				

	
