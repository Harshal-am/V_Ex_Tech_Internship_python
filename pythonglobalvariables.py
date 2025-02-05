x = "cool"
def myfunc():
 print("Python is " + x) 
 
myfunc()

x = "cool"
def myfunc():
 x = "very cool"
 print("Python is " + x)
myfunc()

print("Python is " + x) 
def myfunc():
        global x
x = "very cool"
myfunc()

print("Python is " + x)