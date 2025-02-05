# Convert from JSON to Python
import json
# some JSON:
x = '{ "name":"ramesh", "age":20, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

#Convert from Python to JSON 
import json
# a Python object (dict):
x = {
 "name": "raju",
 "age": 38,
 "city": "noyda"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)

import re
#Check if the string starts with "The" and ends with "Spain":
txt = "The rain in japan"
x = re.search("^The.*japan$", txt)
if x:
 print("YES! We have a match!")
else:
 print("No match") 
