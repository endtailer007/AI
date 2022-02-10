import pandas as pd
import numpy as np
#Data structures in python : Dataframe and series , Dataframe is a two dimensional array of values with both a row and a column index
#A series is a one dimensional array of values with an index examples for both of them are excel sheets
S=pd.Series([1,2,3,4,5])#In Series S should be uppercase
print(S)
print(S.index)
print(S.values)
x=np.array([11,28,72,3,5,8])
print(x)
print(S.values)
#both are of same type
print(type(S.values),type(x))
#This means that Numpy is required by pandas and pandas is built on top of Numpy
students=["MechanicalA","Mechanical B"]
numbers=[64,69]
T=pd.Series(numbers,index=students)
print(T)
T2=pd.Series([12,10],index=students)
print(T+T2)
print("sum of T: ",sum(T))
#The indices do not have to be the same for series addition. The index will be the "union" of the both indices.
#If an index doesn't occur in both series, the value for this series will be NaN
fruits=["peaches","oranges","cherries","pears"]
fruits2=["raspberries","oranges","cherries","pears"]
a=pd.Series([20,33,40,10],index=fruits)
a2=pd.Series([19,13,23,28],index=fruits2)
print(a+a2)
#indices can be completely different, as in the following example
#We have two indices, one is the turkish translation of the english fruit names
Fruits=["apples","oranges","cherries","pears"]
fruits_tr=["elma","portakal","kiraz","armut"]
#Now if we sum these two list as indices we will get NaN in every column
#single and multiindexing
print("single indexing",a["oranges"])
print("multiindexing\n",a[["oranges","cherries"]])
#pandas.series.apply
print(a)
print(a.apply(np.log))
#we can handle missing data in pandas by declaring custom arrays
#.notnull() function will return true if the index has any element and returns false if the index does not have any element
#.dropna() function will remove or drop any null values from the list
#using .fillna(value) we can fill null indexes and .astype(datatype ) allows us to convert one datatype to another datatype
ser1=pd.Series(["a","b","c"])
print(ser1)
print(ser1.map({"a":"Yes","b":"No","c":"Not sure"}))







