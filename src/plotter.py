import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

from .solvers import ODESolver

# This class creates the figure, plots the vector field, and plots the (animated) trajectories   
class Plotter: 
    
    # setup  self.variables
    def __init__(self, System, AxisLimits, DiagramNames=["Diagram", "x-axis", "y-axis", "speed"], **kwargs):
        #System = The system being modeled  
        #AxisLimits = [[xMin, xMax, nx], [yMin, yMax, ny]]
        #figsize = (x,y)

        #If no specific FigSize is entered, default to (10,8)
        self.FigSize = kwargs.get("FigSize")
        if self.FigSize == None: self.FigSize=(10,8)

        #If no specific FigSize is entered, default to viridis
        self.Cmap = kwargs.get("Cmap")
        if self.Cmap == None: self.Cmap ="viridis"

        #plot field and make figsize and ax
        self.fig, self.ax = plt.subplots(figsize=self.FigSize)

        #define variables from parameters
        self.System = System
        self.AxisLimits = AxisLimits
        self.DiagramNames = DiagramNames

        #define variables for later
        self.VectorField = None
        self.TrajectoryLines = []
        self.Animation = None 

    # computes and returns the vector field
    def ComputeVectorField(self):
        #expanding self.AxisLimits for the dimensions of the field
        xMin, xMax, nx = self.AxisLimits[0]
        yMin, yMax, ny = self.AxisLimits[1]

        #creating a meshgrid for the values of x and y
        xRange = np.linspace(xMin, xMax, nx)
        yRange = np.linspace(yMin, yMax, ny)
        x, y = np.meshgrid(xRange, yRange) 

        #make another list to store the vectors 
        xVector = np.zeros_like(x)
        yVector = np.zeros_like(y)

        #for each point, take the derivative of the positon and store in the vector list
        for i in range(nx):
            for j in range(ny):
                vector = self.System.Derivative([x[i,j], y[i,j]]) #uses the derivative function from the class self.System
                xVector[i,j] = vector[0]
                yVector[i,j] = vector[1]

        #calculates magnitude
        magnitude = np.sqrt(xVector**2+yVector**2)
        magnitude[magnitude==0] = 1 #removes divide by 0s. 

        #normalise the vectors 
        U_xVector = xVector / magnitude 
        U_yVector = yVector / magnitude

        #returns the position [x,y], the vectors direction [U_xVector, U_yVector], and the magnitude of the vector (magnitude)
        return x, y, U_xVector, U_yVector, magnitude
    
    #Plot the vector field
    def PlotVectorField(self):
        #get the vector and postion values from the function ComputeVectorField
        x, y, U_xVector, U_yVector, magnitude = self.ComputeVectorField()
       
        #quiver plot for the points and vecotr
        self.VectorField = self.ax.quiver(x, y, U_xVector, U_yVector, magnitude, cmap=self.Cmap, alpha=0.7) #cmap for the colour, alpha for the grid width?

        #adds a colour bar 
        plt.colorbar(self.VectorField, ax=self.ax, label=self.DiagramNames[3])

        #calls the function to set the properties of the figure
        self.SetFigureProperties()

    #sets the properties of the figure
    def SetFigureProperties(self):
        #expanding self.AxisLimits for the dimensions of the field
        xMin, xMax, nx = self.AxisLimits[0]
        yMin, yMax, ny = self.AxisLimits[1]

        #naming 
        self.ax.set_title(self.DiagramNames[0])
        self.ax.set_xlabel(self.DiagramNames[1])
        self.ax.set_ylabel(self.DiagramNames[2])

        #set range
        self.ax.set_xlim(xMin, xMax)
        self.ax.set_ylim(yMin, yMax)

        #grid
        self.ax.grid(True, alpha=0.3)

    # runs TrajectoryCalculator for each given trajectory 
    def MultipleTrajectories(self, TimeSpans, ICs, SolverInfos, PlottingInfos, IsAnimateds):
        #TimeSpans = [[StartTime1, EndTime1], [StartTime2, EndTime2],...]
        #ICs = [[xStart1, yStart1], [xStart2, yStart2],...]
        #SolverInfo = [[SolverMethod1, StepSize1 / dt1], [SolverMethod2, StepSize2 / dt2],...] eg. Rk4Solver or EulerSolver
        #PlottingInfos = [[LineWidth1, Colour1], [LineWidth2, Colour2],...] eg. "red"
        #IsAnimateds = [Boolean1, Boolean2,...] eg. True or False 

        #iterates through each initial condition given 
        for i in range(len(ICs)):
            self.TrajectoryCalculator(TimeSpans[i], ICs[i], SolverInfos[i], PlottingInfos[i], IsAnimateds[i]) #calls TrajectoryCalculator for each trajectory 

    # calculates the trajectory and runs 
    def TrajectoryCalculator(self, TimeSpan, IC, SolverInfo, PlottingInfo, IsAnimated):
        #TimeSpans = [StartTime, EndTime]
        #ICs = [xStart1, yStart]
        #SolverInfo = [SolverMethod, StepSize / dt] eg. Rk4Solver or EulerSolver
        #PlottingInfo = [LineWidth, Colour] eg. "red"
        #IsAnimated = (Boolean) eg. True or False 

        #unpacking SolverInfo 
        SolverName, dt = SolverInfo #dt means stepsize (the change in time per step)

        SolverMethod = ODESolver.Rk4Solver # default solver method 
 
        match SolverName.lower(): #checks the name and fits it with the proper one. 
            case "rk4":
                SolverMethod = ODESolver.Rk4Solver
            case "euler":
                SolverMethod = ODESolver.EulerSolver

        #Calls the selected solver function using the given parameters 
        Time, Trajectory = SolverMethod(self.System, TimeSpan, IC, dt)

        self.TrajectoryPlotter(Time, Trajectory, PlottingInfo, IsAnimated)

    # plots the trajectory with animation 
    def TrajectoryPlotter(self, Time, Trajectory, PlottingInfo, IsAnimated):
        #Time = [Time0, Time1..., Timenx]
        #Trajectory = [[xPos0, yPos0], [xPos1, yPos1],... [xPosnx, yPosny]]
        #PlottingInfo = [LineWidth, Colour] eg. "red"
        #IsAnimated = (Boolean) eg. True or False 

        #unpacking PlottingInfo  
        LineWidth, Colour = PlottingInfo

        #expanding Trajectory
        xPoints = Trajectory[:,0]
        yPoints = Trajectory[:,1]

        #Ensuring LineWidth and Colour are not empty 
        #LineWidth[LineWidth=="N/A"] = 0.3
        #Colour[Colour=="N/A"] = "blue"

        #if IsAnimated is False, make it static 
        if not IsAnimated: 
            self.ax.plot(xPoints, yPoints, color=Colour, linewidth=LineWidth, alpha=0.8)

        #if IsAnimated is True, make it dynamic  
        else: #creates the lists point and line 
            line = self.ax.plot([], [], color=Colour, lw=LineWidth, label="Trajectory")[0]
            point = self.ax.plot([], [], 'bo', markersize=6, label="Current")[0]
            self.ax.legend()

            def animate(frame): #creates the animation function which
                line.set_data([xPoints[:frame]], [yPoints[:frame]]) #line is added from previous
                point.set_data([xPoints[frame]], [yPoints[frame]]) #the point is only the current point
                return line, point 
        
            self.animation = FuncAnimation(self.fig, animate, frames=len(Time), interval=20, blit=True) #animater
            
    def Show(self): #shows the plot 
        plt.show()        