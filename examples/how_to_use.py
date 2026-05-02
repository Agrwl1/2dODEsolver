import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np

from src.simulation import Simulation 

#from systems.(filename) import (classname)
from systems.how_to_add import ODESystem

# PARAMETERS 


# Vector field (mandatory)

# the range and number of vectors for x and y
AxisLimits = [
    [-5,5,41], # xStart, xEnd, nx (number of vectors along the x axis)
    [-5,5,41] # yStart, yEnd, ny (number of vectors along the y axis)

]


# Trajectories (optional)
#it will plot a trajectory for each entry. (only one trajectory can be animated at a time)

# the start time and end time of each trajectory 
TimeSpans = [
    [0,2*np.pi], #startTime1, endTime1
    [1,7] #startTime2, endTime2
]

# the starting position of each trajectory
ICs = [
    [-3.5, -4], #xStart1, yStart1
    [1, 1] #xStart2, yStart2
]

# Solver information
#the solve is not case-sensitive
#I reccommend using below 0.5
SolverInfos = [
    ["RK4", 0.01], #SolverName1, dt1 (stepSize1)
    ["EuLEr", 0.01] #SolverName2, dt2 (stepSize2)
]

# Plot information  
PlottingInfos = [
    [1, "red"], #LineWidth1, LineColour1
    [0.5, "green"] #LineWidth2, LineColour2
]

# Is the function animated
#only 1 function can be animated at a time
IsAnimateds = [
    True, #Boolean1
    False #Boolean2
]

#names of the parts of the diagram 
DiagramNames =  [
    "ODE System name", #diagram name
    "x-axis variable (units)", #x-axis name
    "y-axis variable (name))", #y-axis name
    "magnitude of change of x and y" #colourbar name 
]

#System = (systemsame)
System = ODESystem

sim1 = Simulation(System, AxisLimits, DiagramNames, parameter1=2, FigSize=(10,8), Cmap="managua")

#kwargs accepted: 
#Cmap: viridis (default), plasma, inferno, magma, cividis, winter, etc. 
#FigSize: (10,8), any appopriate value
# (Any that were defined in the system) eg. parameter1=2

sim1.Field() #plots field
sim1.Trajectory(TimeSpans, ICs, SolverInfos, PlottingInfos, IsAnimateds) #plots trajectory
sim1.Show() #shows the plot 