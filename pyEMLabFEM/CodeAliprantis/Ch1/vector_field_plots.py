# (c) Dionysios Aliprantis and Oleg Wasynczuk
# Electric Machines: Theory and Analysis Using the 
#    Finite Element Method
# Example 1.12 - Vector field visualization using Python

import numpy as np
import matplotlib.pyplot as plt

# Problem parameters
Q1 = 2
Q2 = -1
r1 = np.array([-0.5, 0, 0])
r2 = np.array([ 0.5, 0, 0])
z = 0 # we plot the projection of the E-field on this plane 

# Calculate the electric field
nx = ny = 30
xv = np.linspace(-2, 2, nx)
yv = np.linspace(-1.5, 1.5, ny)
Ex = np.zeros((yv.size,xv.size))
Ey = np.zeros((yv.size,xv.size))

for i in range(xv.size):
    x = xv[i]
    for j in range(yv.size):
        y = yv[j]
        r = np.array([x, y, z])
        d1 = np.linalg.norm(r-r1)
        d2 = np.linalg.norm(r-r2) 
        
        # We will not plot the field too close to the charges
        # because the quiver plot will be dominated by these 
        # arrows. We define a minimum distance to exclude points 
        # within a sphere of radius dmin around the charges.
        dmin = 0.15  
        if d1 < dmin or d2 < dmin:
            E1 = [0, 0, 0]
            E2 = [0, 0, 0]
        else:       
            E1 = Q1*(r-r1)/d1**3
            E2 = Q2*(r-r2)/d2**3
        E = E1 + E2
        Ex[j,i] = E[0]
        Ey[j,i] = E[1]
        
# Make the grid
xx, yy = np.meshgrid(xv, yv)

# Plot
fig = plt.figure()
ax = fig.gca()
ax.streamplot(xx, yy, Ex, Ey, color='0.75')
ax.quiver(xx, yy, Ex, Ey, width=.005, pivot = 'mid')
plt.axis('equal')
plt.show()