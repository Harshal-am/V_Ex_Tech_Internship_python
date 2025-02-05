thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist) 

thislist = ["apple", "banana", "cherry"]
print(len(thislist)) 

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist =["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
 print("Yes, 'apple' is in the fruits list") 

#Change data

thislist = ["apple","banana","mango"]
thislist [1:3] = ["sitafal"]
print(thislist)

#addListItems

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) 

thislist = ["apple", "banana", "cherry"]
obito = ["mango", "pineapple", "papaya"]
thislist.extend(obito)
print(thislist) 

thislist = ["apple", "banana", "mango"]
thislist.remove("banana")
print(thislist) 

#Remove Specified Index

thislist = ["apple","banana","mango"]
thislist.pop(2)
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) 

thislist = ["apple","banana","keri"]
del thislist

#Clear the List

thislist = ["apple","banana","keri"]
thislist.clear()
print(thislist)
