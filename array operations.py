import numpy as np
x=np.array([[1,2],[3,4]])
y=np.array([[5,6],[7,8]])
#Element wise operations
#Addition
print(x+y)
print(np.add(x,y))
#subtraction
print(x-y)
print(np.subtract(x,y))
#multiplication
print(x*y)
print(np.multiply(x,y))
#division
print(x/y)
print(np.divide(x,y))
print(np.sqrt(x))
#Matrix operations
#matrix multiplication (it can be done in two ways as shown below)
print(np.dot(x,y))
print(x.dot(y))
#transpose of a matrix
print(x.T)
print(np.sum(y))#This returns the sum of all elements in the matrix
print(np.sum(y,axis=0))#This returns sum of all row elements
print(np.sum(y,axis=1))#This returns sum of all column elements
v=np.array([1,0,1])
print(np.tile(v,(4,1)))#This  stacks 4 copies of v on top of  each other


