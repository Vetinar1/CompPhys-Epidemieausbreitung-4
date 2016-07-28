# Main script that runs the simulation
#
#
#
#

import lib.draw as draw
import lib.initialize as init
import lib.globals as glob
import lib.travel as travel
import lib.infection as inf
import lib.containment as cont
import matplotlib.animation as anim
import matplotlib.pyplot as pyplot
import numpy




#initialize basic setting, loading data, creating connections, creating a SIR population...
print('loading data, please wait \n')
init.initialize()

#asking for choosing containment and calculation method and asking if the probability of travel should depend on state of health
containment=input('Please choose a containment method. Enter the number. Valid: \n 1: none \n 2: quarantine: put a share of the infected get in quarantine \n 3: inoculation: instantly inoculate 10% of all the people when more than 3% are infected \n 4: closing airport of the city with the highest infection rate > 5% \n (Default=1)\n')
glob.method = input("Please choose calculation method. Valid: RK4, Euler, ODE. Default: ODE. \n")
probTravel = input('Should the probability of travel should depend on state of health? (y/n)')

if probTravel=='y':
	inp = float(input('Please type in the share of infected people traveling although they are infected.\n Has to be between 0-1 \n 0: nobody travels when infected \n 1: infected people travel with the same probability as healthy people \n'))
	glob.ptInf=inp

if containment=='2':
	glob.containment='quarantine'
elif containment == '3':
	glob.containment='inoculation'
elif containment == '4':
	glob.containment='closing airports'
else:
	glob.containment='no containment'

#run simulation:
print('simulation is running, please wait \n')
#if quarantine is selected:


notYetCont=True #to make sure that theres only one day with inoculations
for i in range (1,glob.steps+1):
    #travel:
    travel.travelLandAll(i)
    travel.travelAirAll(i)
    
    #expansion because of SIR with the choosen method:
    if glob.method == "RK4":
        inf.infectRK4All(i)

    elif glob.method == "Euler":
        inf.infectEulerAll(i)

    else:
        inf.infectODEsolverAll(i)
    
    #inoculate people once when the option is set:
    if (notYetCont and containment=='3'):
        #start the instant inoculation when there are totaly more then 3% infected people
        if numpy.sum(glob.inf[i])/numpy.sum(glob.population)>0.03:
            print('inoculation at step ',i)
            cont.inoculation(i)
            notYetCont=False
    
    if(notYetCont and containment=='2'):
        if numpy.sum(glob.inf[i])/numpy.sum(glob.population)>0.03:
            cont.quarantine() 
            print('step:',i,' ',glob.quar,'of the infected people are in quarantin')
            notYetCont=False
				
    #close airports when the option is set:        
    elif(containment=='4'):
        #find the city with the highest share of infected people:
        infPerPopulation=glob.inf[i]/glob.population
        worstCity=numpy.argmax(infPerPopulation)
        #close the airport in the worstCity, when the share of infected people is higher than 0.05 in that city. The airport will nor be opended again during the simulation
        if infPerPopulation[worstCity]>0.05:
            cont.closingAirport(worstCity)
            print('day ',i,': ', glob.cities[worstCity],' airport closed')
            
#animation            
animate = input('simulation done, show an animation?(y/n)')           
if animate =='y':
    # Set up figure
    fig = pyplot.figure(figsize=(10, 10))
    # Render animation
    ani = anim.FuncAnimation(fig, draw.update, frames=int(glob.steps/10), init_func=draw.setupMap, repeat=False, interval=50)
    #Show animation
    pyplot.show()







