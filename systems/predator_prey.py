import numpy as np

# This class  provides the parameters, and derivative calculator of the DampedPendulumSystem
class PredatorPreySystem: 

    # establish parameters 
    def __init__(self, a=1.1, b=0.4, c=0.1, d=0.4, **kwargs):
        #a, b, c, d are the different coefficents which effect this differential equation 

        self.a = a
        self.b = b
        self.c = c
        self.d = d

    # take and return the derivative of the current state
    def Derivative(self, State):
        #State = [x prey population, y predator population]
        #Returns the derivative of the prey and predator population[dxdt, dydt]

        x, y = State
        dxdt = (self.a * x) - (self.b * x * y) #Lotka-Volterra Equations
        dydt = (self.c * x * y) - (self.d * y) 

        return np.array([dxdt, dydt])