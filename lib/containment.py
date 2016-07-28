#methods to contain the epidemic

import lib.globals as glob


#put infected peaple in quarantin. 
def quarantine():
	glob.quar=0.7	#the degree of quarantin is set to 0.7 (70% of the infected people are in quarantine)
	return
	
#instantly inoculate 10% of all the people. only suscetible peaple can be inoculated. They become recovered without beeing infected in between
def inoculation(step):
    glob.rec[step]=glob.rec[step]+0.1*glob.sus[step]
    glob.sus[step]=0.9*glob.sus[step]
    return
	
#close an airport by setting all probabilies to zero. a closed airport will not be opened again during the simulation
def closingAirport(cityIndex):
	glob.probabilitiesAir[cityIndex]=0 #nobody can left the city via air
	glob.probabilitiesAir[:,cityIndex]=0 #nobody can get into the city via air
	return