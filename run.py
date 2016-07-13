# Main script that runs the simulation
#
#
#
# testing done


# Import other scripts (Euler, Runge Kutta, ...)
#from lib.travel import *
from lib.auxiliary import *
from lib.travel import *
import numpy



# Ask user whether a new working file temp.csv should be created
# NOTE: program does not work with missing temp.csv!
new_temp = input("Create new temp.csv from resources? \n Note: Program does not work without valid temp.csv \n New temp.csv will be used as source \n [y/n]? \n")

#read data
if new_temp == "y":
    # Create new temp.csv
    inputData = createNewTemp("res/europe.csv")

else:
	# Do not create new temp.csv
	# Read temp.csv to create array
	inputData = readCities("temp.csv")

#define global variables:
global cities,population,landConnections,airConnections
#cities and population from inputData:
cities = inputData['cities']
population = inputData['population']
# Initialize land and air connectins between cities:
landConnections = createLandConnections(inputData)
airConnections = createAirConnections(inputData)
	



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

