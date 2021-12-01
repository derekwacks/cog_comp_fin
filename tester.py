import numpy as np
import json

data = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(data)
y = data.flatten()
print(y)

x = list(map(str, y))
x.reverse()
print(x)

