"""
1. A vector is a 1-dimansonal array that can be represented as 1-dimansonal array in numpy.
2. It is the sequence of values that can  be indexed and sliced like a list.
"""
#1-dimansonal array(vector) example 

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr[0] + arr[2])
print(arr.__index__)