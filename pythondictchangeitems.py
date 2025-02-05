#Change Dictionary Items
thisdict = {
    "brand" : "ford",
    "modal" : "figo",
    "year" : 1973
}
thisdict["year"] = 2019

#add Dictionary items
thisdict = {
    "brand" : "ford",
    "modal" : "figo",
    "year" : 1937
}
thisdict["color"] = "red"
print(thisdict)

#remove Dictionary items
thisdict = {
    "brand" : "ford",
    "modal" : "mustang",
    "year" : 1963
}
thisdict.pop("modal")
print(thisdict)

thisdict = { 
 "brand": "Ford", 
 "model": "Mustang", 
 "year": 1964 
} 
thisdict.popitem() 
print(thisdict)

thisdict = { 
 "brand": "Ford", 
 "model": "Mustang", 
 "year": 1964
} 
thisdict.clear() 
print(thisdict)

