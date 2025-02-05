print("lol i m unknown")

if 5 > 2:
    print ("five is greter than two")
    
x = 5
y = "john"
print(type(x))
print(type(y))

a = 4
A = "sally"

x = y = z = "orange" 
print(x)
print(y)
print(z)

x = "python  "
y = "is "
z = "cool"
print(x+y+z)

x = 5
y = "obito"
print(x,y)

#global variables

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

x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)

a = """heelo i m from leaf village,
can u help me i m lost plz,tell me 
where is my town way to go """
print(a)

b = "hello ,i m obito"
print(b[2:5])

b = "hii , i m rin"
print(b[:5])

b = "ohayo ooniiii channn!"
print(b[-5:-2]) 

a = "obito"
print(a.upper())

a = "RIN"
print(a.lower())

a = "bakaaaa"
print(a.strip())

a = "hay"
print(a.replace("h", "J")) 

a = "obito, rin"
print(a.split(","))

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age)) 

quantity = 3
itemno = 334
price = 39.82 
myorder = "i want {0} pieces of item {1} for {2} dollars."
print(myorder.format(quantity, itemno, price))

txt = "we R the so-called \"vikings\" from the north."

print(10 > 9)
print(10 == 9)
print(10 < 9)
a = 200
b = 33
if b > a:
 print("b is greater than a")
else:
 print("b is not greater than a") 
 
#logical operators
x = 5
print(x > 3 or x < 4)
x = 5
print(not(x > 3 and x < 10))

x = ["apple", "banana"]
print("banana" in x) 

thislist = ["apple", "bananna", "cherry", "mango"]
print(len(thislist))

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
 print("Yes, 'apple' is in the fruits list") 
 
 