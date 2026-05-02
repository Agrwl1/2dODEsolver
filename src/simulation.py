from .plotter import Plotter

# This class calls other classes to make the program run 
class Simulation:

    def __init__(self, System, AxisLimits, DiagramNames, **kwargs):
        self.System = System(**kwargs) #establishes the system and its parameters 
        self.Plotter = Plotter(self.System, AxisLimits, DiagramNames, **kwargs) #stores the class plotter in self 
        
    def Field(self):
        self.Plotter.PlotVectorField() #call and plot the vector field 

    def Trajectory(self, TimeSpans, ICs, SolverInfos, PlottingInfos, IsAnimateds): #call and plot the trajectories 
        self.Plotter.MultipleTrajectories(TimeSpans, ICs, SolverInfos, PlottingInfos, IsAnimateds) #call and plot the trajectories 

    def Show(self): #call and show the function 
        self.Plotter.Show()