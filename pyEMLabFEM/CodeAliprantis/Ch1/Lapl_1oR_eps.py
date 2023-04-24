# (c) Dionysios Aliprantis and Oleg Wasynczuk
# Electric Machines: Theory and Analysis Using the 
#    Finite Element Method
# Example 1.28 - Defining functions in Python

from math import pi
import numpy as np
import matplotlib.pyplot as plt

def Lapl_1oR_eps(R, eps):
    Reps = np.sqrt(np.square(R) + eps**2)
    y = np.divide(-3,np.power(Reps,3)) + \
        np.divide(3*np.square(R),np.power(Reps,5))
    return y   

R = np.linspace(0,1,10000)
eps = [0.001, 0.01, 0.1]
markers = ['o','*','h']
k = 0
for e in eps:
    plt.semilogy(R, -Lapl_1oR_eps(R = R,eps = e), \
                 marker = markers[k], markevery = 500, 
                 color='k')
    k += 1

plt.xlabel(r'$R$')
plt.legend([r'$\epsilon = ' + str(i) + '$' for i in eps])
plt.grid()
plt.show()