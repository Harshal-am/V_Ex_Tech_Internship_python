thisdict =  {
    "brand" : "ford",
    "modal" : "figo",
    "year" : 1973
}
print(thisdict)

thisdict = { 
 "brand": "Ford", 
 "model": "Mustang", 
 "year": 1964, 
 "year": 2020 
} 
print(len(thisdict))

thisdict = { 
 "brand": "Ford", 
 "electric": False, 
 "year": 1964, 
 "colors": ["red", "white", "blue"] 
} 
print(thisdict)

thisdict = { 
 "brand": "Ford", 
 "model": "Mustang", 
 "year": 1964
} 
print(type(thisdict))

thisdict = { 
 "brand": "Ford", 
 "model": "Mustang", 
 "year": 1964 
} 
x = thisdict["model"] 
print(x)

thisdict = { 
 "brand": "Ford", 
 "model": "Mustang", 
 "year": 1964 
} 
x = thisdict.keys() 
print(x)

car = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
x = car.keys() 
print(x) #before the change 
car["color"] = "white" 
print(x) #after the change

thisdict = { 
 "brand": "Ford", 
 "model": "Mustang", 
 "year": 1964 
} 
x = thisdict.values() 
print(x)

thisdict = { 
 "brand": "Ford", 
 "model": "Mustang", 
 "year": 1964 
} 
x = thisdict.items() 
print(x)

thisdict = { 
 "brand": "Ford", 
 "modal": "Mustang", 
 "year": 1964 
}
if "modal" in thisdict:
    print("yes,'modal' is onee of the keys in the thisdict dictionary")
    
