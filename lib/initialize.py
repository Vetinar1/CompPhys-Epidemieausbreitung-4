#initialize settings, load data, define global variables..

import lib.travel as travel
import lib.globals as glob
import numpy





def initialize():
    #initialize all settings, has to be run at first
    connections() 			# read data and initialize connections
    variableParameters()	# define all variable parameters
    probs() 				# compute the arrays with all probabilieties between cities:
    
    return
     
def variableParameters():

    # define all variable parameters:
    glob.steps = 400 	# number of steps for the simulation
    glob.step = 0		# current step
    glob.pt = 0.01 		# probability of travel
    glob.sf = 0.4 		# share of peolple traveling via air
    glob.quar = 0 		# degree of quarantine, has to be between 0-1, 0: no quarantin, 1: all infected people are in quarantin
    glob.ptInf = 1		#share of infected people traveling although they are infected, has to be between 0-1, 0: nobody travels when infected, 1: infected people travel with the same probability as healthy people
    
    
    glob.pf = glob.pt*glob.sf 		#probability of traveling via air    
    glob.pl = glob.pt*(1-glob.sf) 	#probability of traveling via land
    
    
    #basic SIR-population withous any infected people
    glob.sus = numpy.zeros((glob.steps+1,glob.population.size))
    glob.sus[0]=glob.population
    glob.inf = numpy.zeros((glob.steps+1,glob.population.size))
    glob.rec = numpy.zeros((glob.steps+1,glob.population.size))
    glob.dead = numpy.zeros((glob.steps+1,glob.population.size))

    #1000 infected people in London:
    glob.inf[0][list(glob.cities).index('London')]=1000
    glob.sus[0]=glob.sus[0]-glob.inf[0]

     
    
    #define and choose possible diseases:
    disease = input("Please choose disease. Enter the number of the disease. \n Valid: \n 1: influenza (parameters given in the exercise) \n 2: chicken pocks \n 3: ebola (with death) \n(Default=1)\n")

    if disease == '2':
        #parameters for chicken pocks
        glob.beta=2
        glob.gamma=1/5
        glob.mu=3*10**-5
        glob.death=0
        glob.disease='chicken pocks'
    elif disease == '3':
        #parameters for ebola
        glob.beta=0.05
        glob.gamma=1/42
        glob.mu=3*10**-5
        glob.death=0.74/42
        glob.disease='ebola'
    else:
        #parameters of disease given in the excercises:
        glob.beta=0.1
        glob.gamma=0.07
        glob.mu=3*10**-5
        glob.death=0
        glob.disease='influenza (default)'
    print('parameters: \n beta=',glob.beta,'\n gamma=',glob.gamma,'\n mu=',glob.mu,'\n death=',glob.death,'\n')
				
    return    

    

def probs():    
    #create arrays with all probabilieties between cities:
    glob.probabilitiesLand = travel.probabilities(glob.landConnections,glob.pl)
    glob.probabilitiesAir = travel.probabilities(glob.airConnections,glob.pf)
    return
    
    
 
# compute the arrays with all probabilieties between cities:   
def connections():     
     
    #read data:
    glob.inputData = readCities("res/europe.csv")
    
    #cities and population from inputData:
    glob.cities = glob.inputData['cities']
    glob.population = glob.inputData['population']
    

    # Initialize land and air connectins between cities:
    glob.landConnections = travel.createLandConnections(glob.inputData)
    glob.airConnections = travel.createAirConnections(glob.inputData)
    return
    


#read data from file
#returns an array with entries in the form: ('cities', 'population',  'latitude', 'longitude')
def readCities(source):
	#read from file:
    read=numpy.loadtxt(source, skiprows=1, delimiter="," , dtype={'names': ('cities', 'population', 'latitude', 'longitude'), 'formats': ('a20', 'i4', 'f8', 'f8')})
    
    # Remove cities with more than 200k inhabitants
    for city in read:
    	if city['population'] < 200000:
    		numpy.delete(read, city)
     				
	#create an new array filled with zeros
    output=numpy.zeros(len(read),dtype={'names': ('cities', 'population',  'latitude', 'longitude'), 'formats': ('U20', 'i4', 'f8', 'f8')})
	
	#decode Strings:
    names=read['cities']
    for i in range(0, len(names)):
        output['cities'][i]=names[i].decode('UTF-8')
		
	#fill the rest of the output-array with the datas read from the file:
    output['population']=read['population']    
    output['latitude']=read['latitude']
    output['longitude']=read['longitude']

    return output
