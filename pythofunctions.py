def my_function(): 
 print("Hello  i m rin ") 
 
def my_function(): 
 print("Hello i m rin ") 
my_function()

def my_function(fname): 
 print(fname + " Refsnes") 
my_function("Emil") 
my_function("Tobias") 
my_function("Linus")

def my_function(fname, lname): 
 print(fname + " " + lname) 
my_function("Emil", "Refsnes")

def my_function(fname, lname=""):
    print(fname + " " + lname)

# Call the function with one or two arguments
my_function("Emil")  # Output: Emil
my_function("Emil", "Smith")  # Output: Emil Smith

#Arbitrary Arguments, *args

def my_function(*kids): 
 print("The youngest child is " + kids[2]) 
my_function("Emil", "Tobias", "obito")

#Arbitrary Keyword Arguments, **kwargs
def my_function(**kid): 
 print("His last name is " + kid["lname"]) 
my_function(fname = "Tobias", lname = "patel")

#Default Parameter Value
def my_function(country = "obito"): 
 print("I am  " + country) 
my_function("tobi") 
my_function("hashirama") 
my_function()
my_function("lol")

def my_function(x): 
 return 5 * x 
print(my_function(3)) 
print(my_function(5)) 
print(my_function(9))
