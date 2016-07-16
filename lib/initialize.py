#define global variables

import lib.auxiliary as aux
import lib.travel as travel
import lib.globals as glob
import numpy





def initialize():
    #initialize all settings, has to be run at first
    glob.defineGlobals()
    connections() # read data and initialize connections
    variableParameters() # define all variable parameters
    probs() #compute the #arrays with all probabilieties between cities:
    
    return
     
def variableParameters():

    # define all variable parameters:
    glob.steps = 30 #number of steps for the simulation
    glob.pt = 0.1 #probability of travel
    glob.sf = 0.4 # share of peolple traveling via air
    
    
    glob.pf = glob.pt*glob.sf #probability of traveling via air    
    glob.pl = glob.pt*(1-glob.sf) #probability of traveling via land
    
    
    #basic SIR-population withous any infected people
    glob.sus = numpy.zeros((glob.steps+1,glob.population.size))
    glob.sus[0]=glob.population
    glob.inf = numpy.zeros((glob.steps+1,glob.population.size))
    glob.rec = numpy.zeros((glob.steps+1,glob.population.size))


    #1000 infected people in London:
    glob.inf[0][list(glob.cities).index('London')]=1000
    glob.sus[0]=glob.sus[0]-glob.inf[0]

    #parameters of disease:
    glob.beta=0.1
    glob.gamma=0.07
    glob.mu=3*10**-5
    return    

    

def probs():    
    #arrays with all probabilieties between cities:
    #global probabilitiesAir,probabilitiesLand
    glob.probabilitiesLand = travel.probabilities(glob.landConnections,glob.pl)
    glob.probabilitiesAir = travel.probabilities(glob.airConnections,glob.pf)
    return
    
    
    
def connections():     
     
    #read data:
    glob.inputData = aux.readCities("res/europe.csv")
    
    #cities and population from inputData:
    glob.cities = glob.inputData['cities']
    glob.population = glob.inputData['population']
    
    #print(inputData)
    # Initialize land and air connectins between cities:
    glob.landConnections = travel.createLandConnections(glob.inputData)
    glob.airConnections = travel.createAirConnections(glob.inputData)
    return
    
    
