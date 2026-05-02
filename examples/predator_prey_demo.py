import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np

from src.simulation import Simulation 

from systems.predator_prey import PredatorPreySystem


# PARAMETERS 

# Vector field (mandatory)
AxisLimits = [
    [0, 12.5, 41],
    [1, 7, 41]
]

# Trajectories (optional)
TimeSpans = [
    [0,12],
   # [0,2]
]

# Inital x and y coordinates 
ICs = [
    [1.5,1.5],
   # [np.pi/2,0]
]

# Which solver ("Euler" or "RK4"), stepsize(dt)
SolverInfos = [
    ["Rk4", 0.01], 
   # ["euler".Rk4Solver, 0.01]
]

# Line thickness, line colour 
PlottingInfos = [
    [1, "red"],
 #   [2, "red"]
]

#only 1 fuinction can be animated 
IsAnimateds = [
    True, 
    #False
]

#names of the parts of the diagram 
DiagramNames =  [
    "Predator prey model", #diagram name
    "Prey population", #x-axis name
    "Predator population", #y-axis name
    "population change rate" #colourbar name 
]

System = PredatorPreySystem

sim1 = Simulation(System, AxisLimits, DiagramNames, FigSize=(10,8))
#kwargs accepted: FigSize, Cmap, [based on the system]. If not placed, it just uses the default 


sim1.Field() #plots field
sim1.Trajectory(TimeSpans, ICs, SolverInfos, PlottingInfos, IsAnimateds) #plots trajectory
sim1.Show() #shows the plot 