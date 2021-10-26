import numpy as np



x = np.array([0,0,0,0,3,344,5,5,0,222,3,40,0])
y = np.where(x == 0)[0]
print(sum(y))