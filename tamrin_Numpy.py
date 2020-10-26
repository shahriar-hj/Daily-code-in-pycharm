# this code will contain 2 Hours Code based Course in youtube
print('This Code is contain Numpy class')

import numpy as np

a = np.array([1, 3, 5], dtype='int16')
print(a)
b = np.array([1, 2, 3])
print(b)
c = a * b
print(c)
d = np.array([[1, 2.3, 3.2, 5.2, 5.0], [2.3, 3.2, 4.3, 5.6, 9]])
print(d.dtype)
print(d)

# get dimensions and size
print(d.ndim)
print(d.shape)
print(d.dtype)
print(d.itemsize)
print(d.nbytes)

#  element
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a)
print(a.shape)
print(a[1, -2])
print(a[0, 5])
print(a[0, :])
print(a[:, 3])
print(a[0, 6:1:-2])  # 1- starting index:ending index:step size
a[0, 5] = 23
print(a)

# 3D Example
b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(b)
print(b[0, 1, 1])

