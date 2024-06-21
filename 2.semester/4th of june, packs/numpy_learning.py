import numpy as np

np_array = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])
print(np_array[:,[1,3]])

print(np.arange(4,16).reshape(4,3))