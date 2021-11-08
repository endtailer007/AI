import math as m
#Lists
#These are the most widely used datatypes in python
#It can store multiple data types
x=[1,2,3,"hello world","hi"]#slicing operation same as strings can be performed on lists also!
print(x)
#Lists  are immutable hence we can change a particular value of list at a particular place.
print(x[0])
x[0]='25'
print(x)
x[2:3]="Sooraj"#we have given a string hence the value given will be stored as single characters in the list at different locations for different characters
print(x)
x[4:5]=["Sooraj"]#This is a list hence it will be stored at only one location as a whole and not divided into characters.
x.append("new")#This will add the value at the end,you can also append list in a list as we have done in previous case of adding list to a list
print(x)
print(x[4])
x.extend([1,2,3])#Extend will unpack the list and adds each element to the end of the list, we can even use + operator instead of using extend
x=x+[4,5,6 ]
print(x)
x.insert(2,"another")#Insert will add a element at a particular location this will increase the size of the list
print(x)
x.pop()#this will remove the element from the end,pop can also take arguments which will remove the value given the location is the argument
x.pop(1)#This will remove the element at index 1
print(x)
x.remove("hello world")#This will remove the value "hello world" from the list
print(x)#If you try to remove the element which is not in list then it will give us error
print(list(range(10)))#This will print all values from 0 to 9 in the form of a list
for i in range(10):
    print(i)#This prints each values in a new line characters
print("We have come outside the loop")
y=[a for a in range(10)]
print(y)#This prints the given data in the form of a single list, this method is known as list comprehension
y.reverse()#This will reverse the list without any sorting
print(y)
y.sort()#This will automatically sort the list in the ascending order
print(y)
y.sort(reverse=True)#This prints the values of the list in descending order
print(y)
#TWO DIMENSIONAL LISTS
number_sets=[[1,2,3,4],[5,6,7,8],[9,10,11,12,[21,30,35,[2,3,4,5]]]]
print(number_sets)#This prints the whole list
print(number_sets[2])#This prints value at specified index
print(number_sets[2][4])#This will print element at index and elements mentioned in sublist index
#Same operations performed on lists can be done on sublists
cities=['delhi','hyderabad','pune','chennai']
for city in cities:
    print(len(city))#This prints length of each element in list.
#List comprehension using for loop
#Method1
z=range(8)
z_mod_2=[]
for a in z:
    z_mod_2.append(a%2)
print(z_mod_2)#This is one method of adding values to an empty list using iteration
z_mod_1=[a%2 for a in z]#This is another way of entering values into a list using iteration
print(z_mod_1)
x_is2=[m.log(a) for a in z if a%2 !=0]#The loop will execute only for values of a%2!=0 if a%2==0 for loop will not execute and data will not be added to the list
print(x_is2)


























