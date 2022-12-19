# import numpy as np
#
# print('Numpy stands for Numerical Python.')
# # #-------------------------------#
#
# # #Print 4x4 array of zeros numbers
#
# x = np.zeros((4, 4))
# print(x)
#
# # #Print 4x4 array of ones numbers
#
#
# x = np.ones((4, 4))
# print(x)
#
# # #Print 4x4 array of random numbers
#
# x = np.empty((4, 4))
# print(x)
#
# # #Print list to numpy array
#
#
# l = [2, 1, 3, 5, 4]
# x = np.array(l)
# print(x)
# print(x.dtype)
#
# # #Print range of numpy array
#
#
# x = np.arange(1, 100)
# print(x)
# print(type(x))
# print(len(x))
#
# # #Print range of numpy array with step size 10
#
# x = np.arange(1, 100, 10)
# print(x)
#
# # # Print shape of above
# shape = x.shape
# print(shape)
#
# # # Print 10 x 10 shape
# x = np.zeros((10, 10))
# sh = x.shape
# print(sh)
#
# # # Print 4 dimentional array
#
# y = x.reshape((2, 2, 5, 5))
# print(y)
# print(y.dtype)
#
# import numpy as np
#
# a = np.random.randn(10)
# b = np.random.randn(10)
#
# print(a)
# print(b)
#
# c = a + b
# print(c)
# c *= 2
# print(c)

# # Inverse array
# print(a)
# inverse = 1 / a
#
# print(inverse)
#
# # # True false return if condition is matched
# print(a > 0)
#
# # #Print numbers where condition is matched
#
# print(a[a > 0])
#
# x = np.array([1, 4, 2, 5, 7])
# print(x[4])
#
# print(x[x > 3])
#
# print(x[[2, 1]])
# print(x[[1, 2]])
#
# x = np.random.randn(10, 10)
# print(x)
# print(x[0][9])
# print('Print odd rows')
#
# print(x[1:10: 2])
#
# print('Print 4 colums')
#
# print(x[::, 1:5])
#
# print('Print 4 colums and 4 rows')
#
# print(x[1:5, 1:5])

# print('print zeros surrounded by ones')
# x = np.ones((5, 5))
# print(x)
#
# x[1: -1, 1:-1] = 0
#
# print(x)

#
# x = np.array([10, 2, 5, 6, 7, 8])
# y = np.array([2, 4, 2, 4, 8, 8])
#
# print(np.sqrt(x))
#
# print(np.power(x, 2))
#
# print(np.maximum(x, y))
# salary = np.array([10, 20, 0, 40])
# x = np.where(salary <= 10, 50, salary)
# print(x)
#
# x = np.where(salary <= 10, 'Not Okay', 'Okay')
# print(x)
#
# import numpy as np
#
# x = np.array([10, 10, 30, 20, 50, 60, 40])
# print(x.mean())
# print(x.cumsum())  ## adding next to sum
# print(x.cumprod())
# y = x > 10
# print(y)
#
# print(y.any())
#
# # print(sorted(x))
# print(np.unique(x))
#
# x = [1, 3, 5, 7]
# y = [2, 4, 6, 8]
#
# np.save('testx', x)
# loadx = np.load('testx.npy')
#
# # print(loadx)
#
# np.savez('textxy', x=x, y=y)
# loadxy = np.load('textxy.npz')
#
# print(loadxy['x'])
#
#
# x = np.random.randn(3, 2)
# y = np.random.randn(2, 3)
# # print(x.dot(y))
# print(x.transpose())

# # #------- Random number generator ---------

#
# np.random.seed(3)
# print(np.random.normal(size=(3, 3)))

# # #------- Reshaping ---------

# import numpy as np
#
# x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
# y = x.reshape((2, 3, 3))
# print(y)
#
# y = x.reshape((2, 3, -1))
# print(y)
# print(y.ravel())

# # #------- Concate ---------
#
# y = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# arr1 = np.array(y)
# # print(arr1)
# x = [[11, 22, 33], [44, 55, 66], [77, 88, 99]]
#
# arr2 = np.array(x)
# # print(arr2)
#
# # print(np.concatenate((arr1, arr2)))
# # print(np.concatenate((arr1, arr2), axis=0))
# print(np.concatenate((arr1, arr2), axis=1))  # # for column wise concate
