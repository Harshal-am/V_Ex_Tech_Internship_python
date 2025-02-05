#loop
thisdict = { 
 "brand": "Ford", 
 "model": "Mustang", 
 "year": 1964 
} 
for x in thisdict: 
 print(thisdict[x])
 
 thisdict = { 
 "brand": "Ford", 
 "model": "Mustang", 
 "year": 1964 
} 
for x in thisdict.values(): 
 print(x)
 
 thisdict = { 
 "brand": "Ford", 
 "model": "Mustang", 
 "year": 1964 
} 
for x in thisdict.keys(): 
 print(x)
 
 thisdict = { 
 "brand": "Ford", 
 "model": "Mustang", 
 "year": 1964 
} 
for x, y in thisdict.items(): 
 print(x, y)
 
 #Copy Dictionaries
 thisdict = { 
 "brand": "Ford", 
 "model": "Mustang", 
 "year": 1964
} 
mydict = thisdict.copy() 
print(mydict)

#Nested Dictionaries
myfamily = { 
 "child1" : { 
 "name" : "naruto", 
 "year" : 2004 
 }, 
 "child2" : { 
 "name" : "Tobi", 
 "year" : 2007 
 }, 
 "child3" : {
     "name" : "obito", 
 "year" : 2011 
 } 
} 
print(myfamily)

child1 = { 
 "name" : "raju", 
 "year" : 2004 
} 
child2 = { 
 "name" : "Tobirama", 
 "year" : 2007 
} 
child3 = { 
 "name" : "shinigami", 
 "year" : 2011 
} 
myfamily = { 
 "child1" : child1, 
 "child2" : child2,
 "child3" : child3 
} 
print(myfamily)

myfamily = { 
 "child1" : { 
 "name" : "kamlesh", 
 "year" : 2004 
 }, 
 "child2" : { 
 "name" : "uchihaobito", 
 "year" : 2007 
 }, 
 "child3" : { 
 "name" : "raj", 
 "year" : 2011 
 } 
} 
print(myfamily["child2"]["name"])

