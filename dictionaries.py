#Everything in dictionaries is stored in key:value pairs
d={"actor":"nasir","animal":"dog","earth":1,"list":[1,2,3]}
print(d)
#order is not maintained in dictionary
print(d["animal"])
#if the key does not exist in the dictionary it gives error
#we cannot have keys with exact same name instead for a particular key we can have multiple values
#we can add new key:value pairs
d['module']="intro"
print(d["list"][2])#This prints value in list at index 2 of the list
del d["actor"]#This will delete the key:value pair associated with the given key
#element access in loop
for elem in d:
    print("value for key : %s is "% elem,":",d[elem])
d.items()#This will print all keys and values present in the dictionary
for a,b in d.items():
    print("value for key is : %s is %s"%(a,b))








