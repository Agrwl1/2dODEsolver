import numpy as np

class HarmonicOscillator:

    def __init__(self, k=1, **kwargs):
        self.k = k
    
    def Derivative(self, State):
        # [x (displacement), v (velocity)]

        x, v = State
        dxdt = v
        dvdt = -1 * self.k * x #(k is assumed to be a positive constant)

        return np.array([dxdt, dvdt])