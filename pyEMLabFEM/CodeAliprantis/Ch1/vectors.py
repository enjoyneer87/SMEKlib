# (c) Dionysios Aliprantis and Oleg Wasynczuk 
# Electric Machines: Theory and Analysis Using the 
#    Finite Element Method
# Example 1.5 - Vector operations in Python

import numpy as np

# Define a vector as a NumPy array
B = np.array([-0.5, 1.2, 0.5])
print('B =',B)

# Calculate the norm of the vector
normB = np.linalg.norm(B)
print('||B|| =',normB)