f = open(r"E:\V-Ex tech solution\obito.txt", "r")

#File open
f = open("E:\V-Ex tech solution\obito.txt", "r")
print(f.read())

#
f = open("E:\V-Ex tech solution\obito.txt", "r")
print(f.read()) 

f = open("E:\V-Ex tech solution\obito.txt", "r")
print(f.read(5)) 

#
f = open("E:\V-Ex tech solution\obito.txt", "r")
print(f.readline())
print(f.readline())

#close the file
f = open("E:\V-Ex tech solution\obito.txt", "r")
print(f.readline())
f.close() 


#FILE WRITE
f = open("E:\V-Ex tech solution\obito.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("E:\V-Ex tech solution\obito.txt", "r")
print(f.read()) 

f = open("E:\V-Ex tech solution\obito.txt", "w")
f.write("Woops! I have deleted the content!")
f.close() 

f = open("E:\V-Ex tech solution\obito.txt", "r")
print(f.read()) 

#create a new file
f = open("myfile.txt", "w")
f.write("This is some content.")
f.close()

f = open("myfile.txt", "a")
f.write("\nThis is additional content.")
f.close()

#delete file
import os

file_name = "myfile.txt"

if not os.path.exists(file_name):
    f = open(file_name, "x")
    f.write("This is some content.")
    f.close()
else:
    print(f"The file '{file_name}' already exists.")
 
try:
 print(x)
except:
 print("Something went wrong")
finally:
 print("The 'try except' is finished") 