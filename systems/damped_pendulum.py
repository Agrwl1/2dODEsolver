import numpy as np

# This class  provides the parameters, and derivative calculator of the DampedPendulumSystem
class DampedPendulumSystem: 

    # establish parameters 
    def __init__(self, g=10, Length=1, Damping=0, **kwargs):
        #g = the accelaration from gravity
        #Length = is the length of the pendulum
        #Damping = the damping coefficent 

        self.g = g
        self.Length = Length
        self.Damping = Damping

    # take and return the derivative of the current state
    def Derivative(self, State):
        #State = [θ angle, ω angular velocity]
        #Returns the derivative of  the angle and angular velocity [dθdt, dωdt]

        Angle, Omega = State
        dAngledt = Omega
        dOmegadt = -Angle * (self.g / self.Length) - Omega * self.Damping #uses the differential eq to calculate dωdt
        return np.array([dAngledt, dOmegadt])