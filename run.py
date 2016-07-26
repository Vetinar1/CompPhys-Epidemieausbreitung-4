# Main script that runs the simulation
#
#
#
#

import lib.draw as draw
import lib.initialize as init
import lib.globals as glob
import matplotlib.animation as anim
import matplotlib.pyplot as pyplot

glob.method = input("Please choose calculation method. Valid: RK4, Euler, ODE. Default: ODE. \n")
#initialize basic setting, loading data, creating connections, creating a SIR population...
init.initialize()

# Set up figure
fig = pyplot.figure(figsize=(10, 10))
# Render animation
ani = anim.FuncAnimation(fig, draw.update, frames=glob.steps, init_func=draw.setupMap, repeat=False, interval=50)
# Show animation
pyplot.show()



