# Main script that runs the simulation
#
#
#
# testing done


# Import other scripts (Euler, Runge Kutta, ...)
#from lib.travel import *
import lib.auxiliary as aux
import lib.travel as travel
import lib.initialize as init
import lib.globals as glob
import lib.infection as inf


#initialize basic setting, loading data, creating connections, creating a SIR population...
init.initialize()





aux.setupMap(glob.inputData)


i=1
while i<= glob.steps:
    # Run Simulation
    # One step == one day

    # Calculate land + air travel
    #print(glob.sus[i][city])
    travel.travelLandAll(i)
   # print(glob.sus[i][city])
    travel.travelAirAll(i)
    #print(glob.sus[i][city])
    
    # Execute Euler, RK and ode/odeint
#    inf.infectEulerAll(i);
    inf.infectRK4All(i);
#    inf.infectODEsolverAll(i);
    
    i += 1
    

#	infectODEsolverAll();
#	
#	# draw using matplotlib
#	