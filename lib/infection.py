# THE POWER OF MATH
# Implements math (auxiliary) functions

#Import
import numpy
import scipy.integrate as integrate
import lib.globals as glob


#Runge-Kutte method fourth-order and h=1 to solve a differential equation in the form y'(t)=f(y,t) and the given initial values y0 (can also be an array of values) and t0
def RK4(f,y0,t0):
    h = 1
    k1 = f(y0,t0)
    k2 = f(y0+h/2*k1,t0+h/2)
    k3 = f(y0+h/2*k2,t0+h/2)
    k4 = f(y0+h*k3,t0+h)   
    y1 = y0 + h/6*(k1+2*k2+2*k3+k4)
    return y1


#explicit Euler method (one step, h=1) to solve a differential equation in the form y'(t)=f(y,t) and the given initial values y0 (can also be an array of values) and t0
def euler(f,y0,t0):
    h=1
    y1=y0+h*f(y0,t0)
    return y1
    

#procedure using odeint from scipy.integrate to solve a differential equation in the form y'(t)=f(y,t) and the given initial values y0 (can also be an array of values) and t0
def ODEsolver(f,y0,t0):
    h=1
    t1 = t0+h 
    y=integrate.odeint(f,y0,numpy.array([t0,t1]))
    y1=y[-1] #odeint returns an array of solutions, one solution for each t in the given sequence of time points. We are only interested in the last solution 
    return y1


def infectRK4(SIR):
    return RK4(DGLs,SIR,0)


def infectEuler(SIR):
    return euler(DGLs,SIR,0)
 
    
def infectODEsolver(SIR):
    return ODEsolver(DGLs,SIR,0)


#Solve the differential equations for all cities. f is the prefered method to solve the DGLs (infectRK4, infectEuler or infectODEsolver)
def runAll(f,step):
    for i in range(len(glob.cities)):
        SIR = numpy.array([glob.sus[step][i],glob.inf[step][i],glob.rec[step][i]]) 
        SIRnew = f(SIR)
        glob.sus[step][i]=SIRnew[0]
        glob.inf[step][i]=SIRnew[1]
        glob.rec[step][i]=SIRnew[2]
    return 
    
    
def infectRK4All(step):
    runAll(infectRK4,step)
    return
	
 
def infectEulerAll(step):
    runAll(infectEuler,step)
    return
    
	
def infectODEsolverAll(step):
    runAll(infectODEsolver,step)    
    return
 
 
#the given differential equations to describe the spread of diseases. The input variable SIR must be an array: SIR=array([S,I,R])
def DGLs(SIR,t):
    S = SIR[0]
    I = SIR[1]
    R = SIR[2]
    N = S+I+R
    dS = -glob.beta*S*I/N + glob.mu*(N -S)
    dI = glob.beta*S*I/N - glob.gamma*I - glob.mu*I
    dR = glob.gamma*I - glob.mu*R
    return numpy.array([dS,dI,dR])
    

 
