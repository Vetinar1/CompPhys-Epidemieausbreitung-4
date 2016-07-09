# THE POWER OF MATH
# Implements math (auxiliary) functions


#Runge-Kutte method fourth-order and h=1 to solve a differential equation in the form y'(t)=f(t,y) and a given initial value y(t0)=y0 given as a list [t0,y0]
def infectRK4(f,initialValue):
    t0 = initialValue[0]
    y0 = initialValue[1]
    h = 1
    k1 = f(t0,y0)
    k2 = f(t0+h/2,y0+h/2*k1)
    k3 = f(t0+h/2,y0+h/2*k2)
    k4 = f(t0+h,y0+h*k3)
    t1 = t0+h    
    y1 = y0 + h/6*(k1+2*k2+2*k3+k4)
    return [t1,y1]

#explicit Euler method (one step, h=1) to solve a differential equation in the form y'(t)=f(t,y) and a given initial value y(t0)=y0 given as a list [t0,y0]
def infectEuler(f,initialValue):
    t0=initialValue[0]
    y0=initialValue[1]
    print(y0)
    h=1
    t1 = t0+h 
    #print('t1= ', t1)
    y1=y0+h*f(t0,y0)
    print('y1= ',y1)
    return [t1,y1]
    


	
def infectODEsolver(f,y):
	return
	
def infectRK4All():
	return
	
def infectEulerAll():
	return
	
def infectODEsolverAll():
	return
 
 
#the given differential equations to describe the spread of diseases. The input variable SIR must be an array: SIR=array([S,I,R])
def DGLs(t,SIR):
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
    
