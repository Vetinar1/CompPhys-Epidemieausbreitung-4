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


#read data
inputData = readCities("res/europe.csv")

#define global variables:
global cities,population,landConnections,airConnections

#cities and population from inputData:
cities = inputData['cities']
population = inputData['population']
sus = population
inf = numpy.zeroes(sus.size)
rec = inf

# Initialize land and air connectins between cities:
landConnections = createLandConnections(inputData)
airConnections = createAirConnections(inputData)
	

setupMap(inputData)

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
	
