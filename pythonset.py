thisset = {"apple", "banana", "cherry"} 
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"} 
print(thisset) 

thisset = {"apple", "banana", "cherry", True, 1, 2} 
print(thisset)

#get the length of a set
thisset = {"raj", "raju", "rakhesh"} 
print(len(thisset))

#data type

set1 = {"abc", 23, True, 50, "male"}
myset = {"lenovo", "dell", "hp"}
print(type(myset))
thisset= {"lenovo", "dell", "hp"}
thisset.add("acer")
print(thisset)

#remove set

thisset = {"apple", "banana", "cherry"} 
thisset.remove("banana") 
print(thisset)

thisset = {"apple", "banana", "cherry"} 
x = thisset.pop() 
print(x) 
print(thisset)

thisset = {"apple", "banana", "cherry"} 
thisset.clear() 
print(thisset) 

#loop set
thisset = {"apple", "banana", "cherry"} 
for x in thisset: 
 print(x)
 
#join sets

set1 = {"a", "b" , "c"} 
set2 = {1, 2, 3} 
set3 = set1.union(set2) 
print(set3)

#Keep ONLY the Duplicates

x = {"ramlo", "raju", "raj"}
y = {"don", "lol", "obito"}
x .intersection_update(y)
print(x)


x = {"apple", "banana", "cherry"} 
y = {"google", "microsoft", "apple"} 
x.symmetric_difference_update(y) 
print(x)
