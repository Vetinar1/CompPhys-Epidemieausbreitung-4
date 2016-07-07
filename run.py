# Main script that runs the simulation
#
#
#


# Import other scripts (Euler, Runge Kutta, ...)
#from lib.travel import *
from lib.auxiliary import *
import numpy



# Ask user whether a new working file temp.csv should be created
# NOTE: program does not work with missing temp.csv!
new_temp = input("Create new temp.csv from resources? \n Note: Program does not work without valid temp.csv \n New temp.csv will be used as source \n [y/n]? \n")
if new_temp == "y":
	# Create new temp.csv
	createNewTemp("res/europe.csv")

else:
	# Do not create new temp.csv
	# Read temp.csv to create array
	cities = readCities("temp.csv")
	
# Initialize connectins between cities

# Initialize Land connections
# First, create 2D array full of zeros; each row/column index n corresponds to one cities[n]
landConnections = numpy.zeros((cities.size, cities.size))

# Put a 1 in each field corresponding to dist < 500 km <= REWORD THIS
for i in range(cities):
	for j in range(cities):
		# If distance between city and city2 < 500km, create connection
		# NOTE: Distance calculation according to http://www.kompf.de/gps/distcalc.html
		# -> dist = 6378.388 * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon2 - lon1))
		if i == j:
			# Obvious rule patch
			landConnections[i][j] = 0
		else if 6378.388 * numpy.arccos(numpy.sin(cities[i][2]) * numpy.sin(cities[j][2]) + numpy.cos(cities[i][2]) * numpy.cos(cities[j][2]) * numpy.cos(cities[j][3] - cities[i][3])) < 500:
			landConnections[i][j] = 1

# Initialize Air connections
# 


while SIMULATION_RUNNING == True:
	# Run Simulation
	# One while == one day
	
	# Calculate land + air travel
	travelLandAll();
	travelAirAll();
	
	# Execute Euler, RK and ode/odeint
	infectEulerAll();
	infectRK4All();
	infectODEsolverAll();
	
	# draw using matplotlib

