import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np

from src.simulation import Simulation 

from systems.damped_pendulum import DampedPendulumSystem




# PARAMETERS 

# Vector field (mandatory)
AxisLimits = [
    [-2*np.pi, 2*np.pi, 41],
    [-5, 5, 41]
]

# Trajectories (optional)
TimeSpans = [
    [0,10],
   # [0,2]
]

# Inital x and y coordinates 
ICs = [
    [np.pi/4,0],
   # [np.pi/2,0]
]

# Which solver ("Euler" or "RK4"), stepsize(dt)
SolverInfos = [
    ["Rk4", 0.01], 
   # ["euler".Rk4Solver, 0.01]
]

# Line thickness, line colour 
PlottingInfos = [
    [1, "black"],
 #   [2, "red"]
]

#only 1 fuinction can be animated 
IsAnimateds = [
    True, 
    False
]

#names of the parts of the diagram 
DiagramNames =  [
    "Damped Pendulum Phase Space", #diagram name
    "Angle, (rad)", #x-axis name
    "Angular velocity (rad/s)", #y-axis name
    "Watermelon" #colourbar name 
]

System = DampedPendulumSystem

sim1 = Simulation(System, AxisLimits, DiagramNames, FigSize=(10,8), Damping=1)
#kwargs accepted: FigSize, Cmap, [based on the system]. If not placed, it just uses the default 


sim1.Field() #plots field
sim1.Trajectory(TimeSpans, ICs, SolverInfos, PlottingInfos, IsAnimateds) #plots trajectory
sim1.Show() #shows the plot 