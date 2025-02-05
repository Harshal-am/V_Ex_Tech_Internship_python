class MyClass: 
 x = 5 
print(MyClass)

class MyClass: 
 x = 5 
p1 = MyClass() 
print(p1.x)

class Person: 
 def __init__(self, name, age): 
  self.name = name 
  self.age = age 
p1 = Person("John", 36) 
print(p1.name) 
print(p1.age)

class Person: 
 def __init__(self, name, age): 
   self.name = name 
   self.age = age 
p1 = Person("John", 36) 
print(p1)

class Person: 
 def __init__(self, name, age): 
  self.name = name 
  self.age = age 
 def myfunc(self): 
  print("Hello my name is " + self.name) 
p1 = Person("itachi : ) ", 36) 
p1.myfunc()

#delete object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello vatashiva .... " + self.name)

# Create an object of the Person class
p1 = Person("John", 36)

# Delete the 'age' attribute
del p1.age

# Check if 'age' exists before accessing it
if hasattr(p1, 'age'):
    print(p1.age)
else:
    print("The 'age' attribute does not exist.")
    
