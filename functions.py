import math as m
def my_func(x):
    if x%2!=0:
        return(m.log(x))
    else:
        return(x)
x=range(10)
x_is3=[my_func(a) for a in x]#Calling the function with input argument as a which is in range of x.The values are stored in the form of list
print(x_is3)
def mysum(x=10,y=10):
    return(2*x+3*y)
print(mysum(2,3))#Since we mentioned the values here those will be passed to the function instead of the default arguments
print(mysum(2))#We have given only one argument hence it will take other as default
print(mysum())#Since we haven't given any arguments the function will consider default arguments as the actual ones
#LAMBDA FUNCTION
def cube(y):
    return y*y*y
z=lambda a: a*a*a#we can use lambda functions instead of simple function, we need not define anything or calling, it is also called as anonymous function
print(z(4))
print(cube(5))
#We use expection block to bypass exceptions in a program
try:
    age=int(input("Enter your age: "))
except:
    age="There was some error while processing your information."#This will be displayed when we print the age if the user enters any input other than the integers/
print(age)




