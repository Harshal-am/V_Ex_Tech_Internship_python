#Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"] 
thislist.sort()
print(thislist) 

#Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist) 

#Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) 

#Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"] 
thislist.reverse()
print(thislist)

#copy a List
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3) 

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
 list1.append(x)
print(list1)

#List count() Method
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("apple") 
print(x)