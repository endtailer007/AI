import numpy as n
l1=[[1,2],[3,0],[-1,-2]]
l2=n.array(l1)#This is an array creation through numpy
print(l2)
print(l2*2)#This will multiply the value with every element in the array and prints for the same thing if we do it using loops you have to take n number of loops of n dimensional lists
#File handling operations
with open("ai.txt","w") as text_file:#The code which is written within the indentation of this block will be stored or executed in file out of the indentation the file will be closed
    data=text_file.write("Hello you are in a file")
print("Out of file")
text=open("ml.txt","w")#here the file is not closed automatically as in the above case, we need to close the file manually using file_name.close() operation
type=text.write("This is in machine learning file.")
print(type)
text.close()#If the file is not in the same location as the program then we need to mention the complete path of the file where it is located
