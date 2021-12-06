#There are two basic ways  to store data 1.Positional/Linear,2.Nonpositional/Non linear
#Linear is divided into two types, Lists and tuples and Non linear is divided into two types: Sets and dictionaries
#Tuples are only a read only datastructure.Data is entered between () for a tuple
x=("Hello world",1,2,3,"AI")
#You can delete an entire tuple once but you cannot delete elements individually from the tuple.
#SETS
players={"Ms Dhoni","Bumrah","Bhuvi","Virat Kohli","Virat Kohli"}
print(len(players))
print(players)#Duplicate values are not allowed in sets even if we include duplicate values while entering while running it will remove the duplicate element.
#We can perform union and intersection operations on two sets too!
cricketplayers={"abhiram","kaushik","chaitanya","saiteja","rakesh"}
hockeyplayers={"kaushik","chaitanya","arun","ashwin","srikanth"}
cricket_but_not_hockey=cricketplayers.difference(hockeyplayers)
print(cricket_but_not_hockey)
hockey_but_not_cricket=hockeyplayers.difference(cricketplayers)
print(hockey_but_not_cricket)
both=cricketplayers.intersection(hockeyplayers)
print(both)
all=cricketplayers.union(hockeyplayers)
print(all)
#We can add elements into the sets also! that is set is a mutable data structure, whereas tuple is immutable
#The difference between sets and dictionaries is that dictionaries have keys to which values are to be assigned where as in sets we dont have keys
student={
    "name": "Sooraj",
    "college":"Vasavi college of Engineering",
    "branch":"Mechanical",
    "year":3,
    "roll": 160219736100
}
print(student["name"])
#We can even add new values to the dictionary

