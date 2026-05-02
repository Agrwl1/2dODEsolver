# Second-order differential equations solver

A modular, object-oriented tool that allows for the calculation and visualisation of any 2D dynamic system. This includes:
 - RK4 and Euler numerical solvers
 - Quiver plot with a colour-coded speed
 - Animated trajectories (via matplotlib FuncAnimations)
 - Easy to extend: simply by adding a class with a 'Derivative(state)' function

Installation (execute the following)
 - git clone https://github.com/yourusername/ode-plotter.git
 - cd ode-plotter
 - pip install -r requirements.txt 

Adding a new system
 - To add a new system, you must create a file under 'systems'
 - You must then create a class of the desired system
 - Following this, you must create a 'Derivative(state)' function (with optional parametrs)
 - For clarification on the building and usage of a new system, consult the following files: systems.how_to_add.py, examples.how_to_use.py

Remarks
 - Inspired by my study of MIT 18.03 (differential equations)
 - This was my first time coding anything independently, and I found the process to be really fun. I learned a lot, and I hope to do more projects like this in the future. 
