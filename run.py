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
import matplotlib.animation as anim
import matplotlib.pyplot as pyplot
import numpy
import scipy

#initialize basic setting, loading data, creating connections, creating a SIR population...
init.initialize()

glob.step = 0
def update(bla):
	
	pyplot.clf()
	glob.step+=1
	travel.travelLandAll(glob.step)
	travel.travelAirAll(glob.step)
	inf.infectRK4All(glob.step)
	#pyplot.axes(glob.ax)
	#glob.ax = pyplot.axes([-13, 34, 44+13, 72-34])
	#glob.ax.set_alpha(0.5)
	#new_ax = pyplot.axes([0, 0, 1, 1])#[-13, 34, 44+13, 72-34])
	#new_ax.set_axis_bgcolor((0, 0, 0, 0))
	#new_ax.set_autoscale_on(True)
	grid_x, grid_y = numpy.mgrid[-13:44:1000j, 34:72:1000j]
	zgrid = scipy.interpolate.griddata( (glob.inputData["longitude"], glob.inputData["latitude"]), glob.inf[glob.step]/glob.population, (grid_x, grid_y), method="linear")
	#print(glob.inf[glob.step])
	glob.cont = glob.m.contourf(grid_x, grid_y, zgrid, vmin=0)#, alpha=0.5, cmap="YlOrRd")
	glob.m.drawcoastlines()
	glob.m.plot(glob.inputData["longitude"], glob.inputData["latitude"], "r.")
	colorbar = glob.m.colorbar(glob.cont, location="right")
	pyplot.text(5, 70, glob.step)

#m = aux.setupMap()
fig = pyplot.figure(figsize=(10, 10))
#ax0 = pyplot.axes()
ani = anim.FuncAnimation(fig, update, frames=glob.steps, init_func=aux.setupMap, repeat=False, interval=50)
pyplot.show()


'''
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
#    inf.infectRK4All(i);
    inf.infectODEsolverAll(i);
    i += 1
    print(glob.inf[0])

#	infectODEsolverAll();
#	
#	# draw using matplotlib
#	


aux.draw(m)

'''
