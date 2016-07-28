#define global variables

import lib.travel as travel
import lib.globals as glob
import numpy





def initialize():
    #initialize all settings, has to be run at first
    connections() 			# read data and initialize connections
    variableParameters()	# define all variable parameters
    probs() 				# compute the #arrays with all probabilieties between cities:
    
    return
     
def variableParameters():

    # define all variable parameters:
    glob.steps = 100000 	# number of steps for the simulation
    glob.step = 0		# current step
    glob.pt = 0.1 		# probability of travel
    glob.sf = 0.3 		# share of peolple traveling via air
    
    
    glob.pf = glob.pt*glob.sf 		#probability of traveling via air    
    glob.pl = glob.pt*(1-glob.sf) 	#probability of traveling via land
    
    
    #basic SIR-population withous any infected people
    glob.sus = numpy.zeros((glob.steps+1,glob.population.size))
    glob.sus[0]=glob.population
    glob.inf = numpy.zeros((glob.steps+1,glob.population.size))
    glob.rec = numpy.zeros((glob.steps+1,glob.population.size))


    #1000 infected people in London:
    glob.inf[0][list(glob.cities).index('London')]=1000
    glob.sus[0]=glob.sus[0]-glob.inf[0]

    #parameters of disease:
    glob.beta=1#0.1
    glob.gamma=0.0001#0.07
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
    glob.inputData = readCities("res/europe.csv")
    
    #cities and population from inputData:
    glob.cities = glob.inputData['cities']
    glob.population = glob.inputData['population']
    
    #print(inputData)
    # Initialize land and air connectins between cities:
    glob.landConnections = travel.createLandConnections(glob.inputData)
    glob.airConnections = travel.createAirConnections(glob.inputData)
    return
    


#Prozdur zum Einlesen der Daten aus den csv-Dateien.
#Gibt ein Array mit dem jeweiligen Name der Stadt ('cities'), der Anzahl gesunder Leute (hier noch gleich der Einwohnerzahl) ('S'),
#der Anzahl kranker Leute (hier noch 0) ('I'), der Anzahl immuner Leute (hier noch 0) ('R'), 
#dem Breitengrad ('latitude') und dem Längengrad ('longitude') aus <- In Subarrays
def readCities(source):
	#read from file:
    read=numpy.loadtxt(source, skiprows=1, delimiter="," , dtype={'names': ('cities', 'population', 'latitude', 'longitude'), 'formats': ('a20', 'i4', 'f8', 'f8')})
    
    # Remove cities with more than 200k inhabitants
    for city in read:
    	if city['population'] < 200000:
    		numpy.delete(read, city)
     
	#create an new array filled with zeros with the additional field for 'I' and 'R'
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
