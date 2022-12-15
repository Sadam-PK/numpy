import numpy as np

print('Numpy stands for Numerical Python.')
# #-------------------------------#

# #Print 4x4 array of zeros numbers

x = np.zeros((4, 4))
print(x)

# #Print 4x4 array of ones numbers


x = np.ones((4, 4))
print(x)

# #Print 4x4 array of random numbers

x = np.empty((4, 4))
print(x)

# #Print list to numpy array


l = [2, 1, 3, 5, 4]
x = np.array(l)
print(x)
print(x.dtype)

# #Print range of numpy array


x = np.arange(1, 100)
print(x)
print(type(x))
print(len(x))

# #Print range of numpy array with step size 10

x = np.arange(1, 100, 10)
print(x)

# # Print shape of above
shape = x.shape
print(shape)

# # Print 10 x 10 shape
x = np.zeros((10, 10))
sh = x.shape
print(sh)

# # Print 4 dimentional array

y = x.reshape((2, 2, 5, 5))
print(y)
print(y.dtype)
