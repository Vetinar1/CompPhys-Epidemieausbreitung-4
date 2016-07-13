# Implements travel (auxiliary) functions

import numpy


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
			if i == j:
				# Obvious rule patch
				landConnections[i][j] = 0
			elif 6378.388 * numpy.arccos(numpy.sin(inputData[i][2]) * numpy.sin(inputData[j][2]) + numpy.cos(inputData[i][2]) * numpy.cos(inputData[j][2]) * numpy.cos(inputData[j][3] - inputData[i][3])) < 500:
				landConnections[i][j] = 1
				print('groesser!')
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
	

def travelLand():
	return


def travelAir():
	return
	
	
def travelLandAll():
	return
	
	
def travelAirAll():
	return
	

