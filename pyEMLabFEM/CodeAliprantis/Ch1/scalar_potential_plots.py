# (c) Dionysios Aliprantis and Oleg Wasynczuk
# Electric Machines: Theory and Analysis Using the 
#    Finite Element Method
# Example 1.13 - Scalar field visualization using Python

import numpy as np
import matplotlib.pyplot as plt

# Problem parameters
Q1 = 2
Q2 = -1
r1 = np.array([-0.5, 0, 0])
r2 = np.array([ 0.5, 0, 0])
z = 0 # we plot the potential on this plot

# Calculate the electric potential
nx = ny = 100
xv = np.linspace(-2, 2, nx)
yv = np.linspace(-1.5, 1.5, ny)
Phi = np.zeros((yv.size,xv.size))

for i in range(xv.size):
    x = xv[i]
    for j in range(yv.size):
        y = yv[j]
        r = np.array([x, y, z])
        Phi1 = Q1/np.linalg.norm(r-r1)
        Phi2 = Q2/np.linalg.norm(r-r2)
        Phi[j,i] = Phi1 + Phi2
        
# Make the grid
xx, yy = np.meshgrid(xv, yv)

# Define contour values
V = [-12, -6, -2, -1, -0.5, -0.25, 0, \
     0.25, 0.5, 0.75, 1, 1.5, 2, 6, 12]

# Plot
fig = plt.figure()
ax = fig.gca()
CS = ax.contour(xx, yy, Phi, V, colors='k')
plt.axis('equal')
plt.clabel(CS, inline=1, fontsize=12, fmt = '%.2f', manual=True)
plt.show()