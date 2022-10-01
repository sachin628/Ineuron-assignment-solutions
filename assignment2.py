#1. Write a python script to add comments and print “Learning Python” on screen.
    # this is a comment
print("Learning Python")
 

#2. Write a python script to add multi line comments and print values of four variables, each in a new line.
#  Variable contains any values.
""""  this is a multi line comment
  ...................................
  ...................................
 ..............                       """
X= 'Ram'
Y = 20.2
Z= 52
A= 'SD20'
print(X, Y, Z, A, sep='\n')


#3. Write a python script to print types of variables. Create 5 variables each of them containing different types of data.
#  (like 35, True, “MySirG”,5.46, 3+4j, etc)
x= 35
y =  True
Z= "MySirG"
A= 5.46
B= 3+4j
C= "CF5"
print(x, y, Z,A, B, C, sep='\n')

#4. Write a python script to print the id of two variables containing the same integer values.
A=25
B=55
print(id(A))
print(id(B))


#5. Create four variables in a Python script and assign values of different data types to
#them. Write a Python script to print value, its type and id of each variable
x= 35
y =  True
Z= "MySirG"
B= 3+4j
print(x, id(x), type(x))
print(y, id(y), type(y))
print(Z, id(Z), type(Z))
print(B, id(B), type(B))


#6. Write a python script to print all the keywords
import keyword
print(keyword.kwlist)
#7. On Python shell use help() function and display the list of keywords
  #    help> keywords

#8. Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some value to it. Write a python 
# script to import A1 module in A0 and print value of the variable created in A0.py
import A1
print(A1.X)

#9. Name the keywords, used as data in the Python script.
#      True  False   None


#10. Write a python script to display the current date and time. First create variables to 
# store date and time, then display date and time in proper format (like: 13-8-2022 and9:00 PM)
from datetime import datetime as dt
x = dt.now().isoformat()
print(x)