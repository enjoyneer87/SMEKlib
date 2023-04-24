# (c) Dionysios Aliprantis and Oleg Wasynczuk
# Electric Machines: Theory and Analysis Using the 
#    Finite Element Method
# Example 1.6 - Dot product using NumPy

import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])
c = np.dot(a,b)
print('a.b =',c)