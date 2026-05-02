import numpy as np 

class ODESystem:

    def __init__(self, parameter1=1, parameter2=0.5, **kwargs): #add any parameters used
        #establish any parameters used to self 

        self.parameter1 = parameter1
        self.parameter2 = parameter2


    def Derivative(self, State):
        #State = [x,y]
        #Returns the derivative of the vector field at this point [dxdt, dydt] HAS TO BE AN NUMPY ARRAY

        x, y = State
        #store the variables into x and y

        #write the formula for calculating the derivatives of x and y
        dxdt = x - y * self.parameter1
        dydt = x * y * self.parameter2

        #ensure you are returning a np array
        return np.array([dxdt, dydt])

