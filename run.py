# Main script that runs the simulation
#
#
#


# Import other scripts (Euler, Runge Kutta, ...)
from lib.Euler, lib.Runge-Kutta import *
from lib.travel import *

# Load data
# Use https://docs.python.org/3/library/csv.html
# Name, Format?

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

