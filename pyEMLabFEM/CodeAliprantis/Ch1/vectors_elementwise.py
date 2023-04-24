# (c) Dionysios Aliprantis and Oleg Wasynczuk
# Electric Machines: Theory and Analysis Using the 
#    Finite Element Method
# Example 1.7 - Element-wise operations on vectors in Python

import numpy as np

Bx = np.array([ 1, 0, 3])
By = np.array([-1, 2, 4])
normB = np.sqrt(np.square(Bx) + np.square(By))
print('||B|| =',normB)