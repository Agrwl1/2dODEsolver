import numpy as np

# This class provides numerical solvers to ODEs including the following: Euler's method, Range-Kutta 4 method
class ODESolver: 

    #Euler solver least amount of processing time 
    def EulerSolver(System, TimeSpan, IC, dt):
        #TimeSpan = [StartTime, EndTime]    
        #IC (Initical conditions) = [xStart, yStart]
        #dt = (stepsize)
        
        StartTime, EndTime = TimeSpan #Unpacking TimeSpan list  
        TotalTime = EndTime - StartTime #calculates the total time 
        n_steps = int(TotalTime/dt) + 1 #the + 1 makes it include both starting and ending 

        #creating a list to store the calculated time and trajectory 
        Time = np.zeros(n_steps) 
        Trajectory = np.zeros((n_steps, 2))

        #Establishes starting conditions in Time and Trajectory
        Time[0] = StartTime 
        Trajectory[0] = IC 

        #Euler's step
        for i in range(n_steps-1): 

            #using Euler's approximation  
            kF = System.Derivative(Trajectory[i])

            #Incrementing Time and trajectory position 
            Time[i+1] = Time[i] + dt
            Trajectory[i+1] = Trajectory[i] + kF * dt

        return Time, Trajectory 

    #Range-Kutta 4 soolver, more processing time for more accurate results
    def Rk4Solver(System, TimeSpan, IC, dt):
        #TimeSpan = [StartTime, EndTime]    
        #IC (Initical conditions) = [xStart, yStart]
        #dt = (stepsize)
        
        StartTime, EndTime = TimeSpan #Unpacking TimeSpan list  
        TotalTime = EndTime - StartTime #calculates the total time 
        n_steps = int(TotalTime/dt) + 1 #the + 1 makes it include both starting and ending 

        #creating a list to store the calculated time and trajectory 
        Time = np.zeros(n_steps) 
        Trajectory = np.zeros((n_steps, 2))

        #Establishes starting conditions in Time and Trajectory
        Time[0] = StartTime 
        Trajectory[0] = IC 

        #Euler's step
        for i in range(n_steps-1): 

            #Using Rk4 Approximation 
            k1 = System.Derivative(Trajectory[i])
            k2 = System.Derivative(Trajectory[i] + 0.5*k1*dt)
            k3 = System.Derivative(Trajectory[i] + 0.5*k2*dt)
            k4 = System.Derivative(Trajectory[i] + k3*dt)
            kF = (k1+2*k2+2*k3+k4)/6

            #Incrementing Time and trajectory position 
            Time[i+1] = Time[i] + dt
            Trajectory[i+1] = Trajectory[i] + kF * dt

        return Time, Trajectory 