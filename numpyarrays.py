import numpy as np
import time
import math
import sys
S=range(1000)
print(S)
print(sys.getsizeof(S))
print(sys.getsizeof(S)*len(S))
D=np.arange(1000)
print(D.size*D.itemsize)
b=np.array([1,2,3])
print(b.itemsize)#with itemsize you can calculate the size of each element
print(b)
a=np.array([(1,2,3),(4,5,6)])#This is a multidimensional array specifically two dimensional
print(a)
# We use python numpy array instead of a list becouse of the below reasons:
#less memory,fast,convinient.
print(a.size)#returns total no.of elements in the array
print(a.shape)#Since it is a 2*3 matrix it shows (2,3)
#RESHAPING(switching rows and columns)
x=np.array([(8,9,10 ),(11,12,13),(10,11,12),(15,17,18),(20,21,22)])
print("old-->",x)
#x=x.reshape(3,2)
print("new-->",x)
print(x.dtype)#You can find the data type of elements that are stored in the array.So, if you want to know the datattype of a particular element,you can use the dtype function which will print data type along with size.
#SLICING
print(x[1,1])#Here in the x (8,9,10) has index of zero and (11,12,13) has index 1 and each element index in that list starts from zero i.e.,[0,1] denotes  9
print(x)
print(x[0:,2])#This will print second elements from all the rows since we did not specify which column it belongs to
print(x[0:3,1])#Here 3 indicates the index+1 of the array and 1 indicates the index of element of number to be printed from each array,i.e,. it will print elements at a specified index from the first three arrays
#   LINSPACE it is another operation in python numpy which returns evenly spaced numbers over a specified interval it is analogous to arithmetic progression in mathematics
y=np.linspace(1,100,10)
print(y)
#MAXIMUM, MINIMUM, MEAN, SUM ,SQUARE ROOT,STANDARD DEVIATIONS
#one dimensional array
z=np.array([19,23,56,10,19,76,84,90,12])
print(z.min())#returns min value from the array
print(z.max())#returns max value from the array
print(z.sum())#returns sum of the elements in the array
print(z.mean())#returns mean or average of the array
print(np.sqrt(z))#returns array of the square roots of each of the elements
print(np.std(z))#returns standard deviation of the array elements
print(np.median(z))#returns median of the array elements
#for two dimensional arrays
v=np.array([(8,9),(10,11),(12,13)])
print(v.min())
print(v.max())
print(v.sum())
print(v.mean())
print(np.sqrt(v))
print(np.std(v))
print(np.median(v))
#for flattened arrays(similar to nested arrays
arr=[[14,17,12,33,44],
     [15,6,27,8,19],
     [23,2,54,1,4]]
#median of the flattened array
print("\n median of arr,axis=None: ",np.median(arr))
print("\n mean of arr,axis=None: ",np.mean(arr))
#median along axis=0 i.e., column wise operation on the array
print("\n median of arr, axis=0: ",np.median(arr,axis=0))
print("\n mean of arr, axis=0: ",np.mean(arr,axis=0))
#median and mean along axis=1 i.e., row wise operation on the array
print("\n median of arr, axis=1",np.median(arr,axis=1))
print("\m mean of arr, axis=1: ",np.mean(arr,axis=1))
out_arr=np.arange(3)
print("\nout arr: ",out_arr)
print("median of arr,axis=1: ",np.median(arr,axis=1,out=out_arr))
#Mathematical operations on arrays
X=np.array([(1,2,3),(3,4,5)])
Y=np.array([(1,2,3),(3,4,5)])
print(X+Y)
print(X-Y)
print(X*Y)
print(X/Y)
#Vertical and horizontal stacking
print(np.vstack((X,Y)))#stacks arrays vertically one after the other
print(np.hstack((X,Y)))#stack arrays horizontallly
#Ravel (it converts array into list
print(X)
A=X.ravel()#ravel changes the master elements or modifies it .
A[0]=11
B=X.flatten()#flatten doesnot change or modify the master elements it only changes or modifies the elements of the copy of the master array
B[0]=22
J= np.full((3,3),math.pi)#full creates a n by n  matrix(here n value is 3) in this case all 9 values are filled by 3.14
print(J)
K=np.eye(5)#Eye creates a n by n identity matrix i.e., diagonal elements of the matrix would be 1 and remaining elements would be zero
print(K)
L=np.random.random((4,3))#this generates a 4 by 3 matrix with all matrix elements filled randomly between 0 and 1 i.e.,  float elements between 0 and 1 are filled
print(L)
p=np.random.randint(1,5,(4,4))#This prints a 4 by 4 matrix with elements in the range of 1 and 5
print(p)





















