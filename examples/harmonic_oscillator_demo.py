import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np

from src.simulation import Simulation 

from systems.harmonic_oscillator import HarmonicOscillator

# PARAMETERS 

# Vector field (mandatory)
AxisLimits = [
    [-5,5,41],
    [-5,5,41]
]

# Trajectories (optional)
TimeSpans = [
    [0,2*np.pi]
]

# Inital x and y coordinates 
ICs = [
    [-2, 0]
]

# Which solver ("Euler" or "RK4), stepsize(dt)
SolverInfos = [
    ["RK4", 0.1]
]

# Line thickness, line colour 
PlottingInfos = [
    [1, "red"]
]

#only 1 fuinction can be animated 
IsAnimateds = [
    True
]

#names of the parts of the diagram 
DiagramNames =  [
    "Rk4 and Euler comparison (harmonic oscillator)", #diagram name
    "Displacement (m)", #x-axis name
    "Velocity (m/s)", #y-axis name
    "magnitude of change rate" #colourbar name 
]

System = HarmonicOscillator

sim1 = Simulation(System, AxisLimits, DiagramNames, FigSize=(10,8), Cmap="inferno")
#kwargs accepted: FigSize, Cmap, [based on the system]. If not placed, it just uses the default 
#Cmap: viridis (default), plasma, inferno, magma, cividis

sim1.Field() #plots field
sim1.Trajectory(TimeSpans, ICs, SolverInfos, PlottingInfos, IsAnimateds) #plots trajectory
sim1.Show() #shows the plot 