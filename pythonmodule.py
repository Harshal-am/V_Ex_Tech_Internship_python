import mymodule

mymodule.greeting("obito__uchiha")

#variable in module
import mymodule
a = mymodule.person1["age"]
print(a) 

#re-nameing module
import mymodule as mx
a = mx.person1["age"]
print(a)

#built in module
import platform
x = platform.system()
print(x) 

#Using the dir() Function
import platform
x = dir(platform)
print(x)

from mymodule import person1
print (person1["age"]) 

#datetime
import datetime
x = datetime.datetime.now()
print(x)

import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A")) 
