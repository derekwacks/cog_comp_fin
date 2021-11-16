import numpy as np

orig = np.array([[0,1],[2,3]])

ok = orig.flatten()  # flatten 2D numpy array
h = list(map(str, ok))  # convert to list of type str

print(h)