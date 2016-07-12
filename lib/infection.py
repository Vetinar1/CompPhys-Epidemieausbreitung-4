# THE POWER OF MATH
# Implements math (auxiliary) functions

#Import
import numpy
import scipy.integrate as integrate

#Runge-Kutte method fourth-order and h=1 to solve a differential equation in the form y'(t)=f(y,t) and the given initial values y0 (can also be an array of values) and t0
def infectRK4(f,y0,t0):
    h = 1
    k1 = f(y0,t0)
    k2 = f(y0+h/2*k1,t0+h/2)
    k3 = f(y0+h/2*k2,t0+h/2)
    k4 = f(y0+h*k3,t0+h)   
    y1 = y0 + h/6*(k1+2*k2+2*k3+k4)
    return y1

#explicit Euler method (one step, h=1) to solve a differential equation in the form y'(t)=f(y,t) and the given initial values y0 (can also be an array of values) and t0
def infectEuler(f,y0,t0):
    h=1
    y1=y0+h*f(y0,t0)
    return y1
    


#procedure using odeint from scipy.integrate to solve a differential equation in the form y'(t)=f(y,t) and the given initial values y0 (can also be an array of values) and t0
def infectODEsolver(f,y0,t0):
    h=1
    t1 = t0+h 
    y=integrate.odeint(f,y0,numpy.array([t0,t1]))
    y1=y[-1] #odeint returns an array of solutions, one solution for each t in the given sequence of time points. We are only interested in the last solution 
    return y1


#Solve the differential equations for all cities. f is the prefered method to solve the DGLs (infectRK4, infectEuler or infectODEsolver)
def runAll(f):
    for city in cities:
        SIR = numpy.array([city[1],city[2],city[3]]) 
        SIRnew = f(DGLs,SIR,0)
        for i in range(1,3):
            city[i]=SIRnew[i-1]
    return
    
    
    
def infectRK4All():
    runAll(infectRK4)
    return
	
 
def infectEulerAll():
    runAll(infectEuler)
    return
    
	
	
def infectODEsolverAll():
    runAll(infectODEsolver)    
    return
 
 
#the given differential equations to describe the spread of diseases. The input variable SIR must be an array: SIR=array([S,I,R])
def DGLs(SIR,t):
    S = SIR[0]
    I = SIR[1]
    R = SIR[2]
    N = S+I+R
    dS = -beta*S*I/N + mu*(N -S)
    dI = beta*S*I/N - gamma*I - mu*I
    dR = gamma*I - mu*R
    return numpy.array([dS,dI,dR])
    
#ein paar Testwerte:
gamma=0.07
mu=3*10**(-5)
beta=0.1

test1=numpy.array([100000., 0., 0.])
test2=numpy.array([10**6,100,0])
    
