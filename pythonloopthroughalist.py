thislist = ["apple", "banana", "cherry"]
for x in thislist:
 print(x) 

#Loop Through the Index Numbers

thislist = ["apple","mango","sitafal"]
for i in range(len(thislist)):
    print(thislist[i])
    
#Looping Using List Comprehension
    
thislist = ["apple","banana","cherry"]
[print(x) for x in thislist]

fruites = ["mango","apple","banana","sitafal","kiwi"]
newlist = []

for x in fruites:
    if "a" in x:
        newlist.append(x)
        
#Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)