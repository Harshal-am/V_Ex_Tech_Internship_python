thistuple = ("keri","sitafal","mango")
print(thistuple)

#Allow Duplicates
thistuple = ("apple", "mango", "cherry", "apple", "cherry") 
print(thistuple)

#Tuple length
thistuple = ("apple", "banana", "cherry") 
print(len(thistuple))

#Create Tuple With One Item

thistuple = ("apple",) 
print(type(thistuple)) 
#NOT a tuple 
thistuple = ("apple") 
print(type(thistuple))

#Data type
thistuple = ("apple", "banana", "cherry") 
print(thistuple[1]) 

thistuple = ("apple", "banana", "cherry") 
print(thistuple[-1]) 

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango") 
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry") 
if "apple" in thistuple: 
 print("Yes, 'apple' is in the fruits tuple")
 
 #update tuple
 x = ("apple","sitafal","cherry")
 y = list(x)
 y[1] = "keri"
 x = tuple(y)
 print(x)
 
 thistuple = ("apple", "banana", "cherry") 
y = list(thistuple) 
y.append("orange") 
thistuple = tuple(y)
 
 #Remove items
thistuple = ("apple", "banana", "cherry") 
y = list(thistuple) 
y.remove("apple") 
thistuple = tuple(y)

#Loop Through a Tuple
thistuple = ("apple", "banana", "cherry") 
for x in thistuple: 
 print(x)
 
thistuple = ("apple", "banana", "cherry") 
for i in range(len(thistuple)): 
 print(thistuple[i])
 
 #join two tuple
 tuple1 = ("a", "b" , "c") 
tuple2 = (1, 2, 3) 
tuple3 = tuple1 + tuple2 
print(tuple3)

#multiply tuple
fruits = ("apple", "banana", "cherry") 
mytuple = fruits * 2
print(mytuple)
