# 1. Creating a variable

a = 1
b = 2
sum = a + b

print(sum)


# 2.casting variable

a = int(3)
b = str(3)
c = float(3)

print(a)
print(b)
print(c)


# 3. Get type of variable

a = 10
b = "ayesha"
c = 3.45

print(type(a))
print(type(b))
print(type(c))


# 4. Single or double quote for variable

a = "Ayesha"

b = 'Ayesha'

print (a)
print(b)


# 5. Case sensitive of variable

a = "Ayesha"
A = "Ayesha"


# 6. Rules to write a variable name

name = "Ayesha"
Name = "Ayesha"
_name = "Ayesha"

# 7. camel case of variable name

myVariableName = "Ayesha"

# 8. pascal case of variable name


MyVariableName = "Ayesha"

# 9. snake case of variable name

My_Variable_Name = "Ayesha"


# 10. Assigning many values to variable

a, b, c = "Apple", "Mango", "Banana"

print(a)
print(b)
print(c)


# 11. Assigning one value to many variable

a = b = c = "Ayesha"
print(a)
print(b)
print(c)


# 12. Unpack a collection of variable

name = ["ayesha", "ameena", "alina"]
a , b , c = name 
print(a)
print(b)
print(c)


# 13. Output variable example 1

a = "My name is Ayesha"
print(a)


# 14. Output variable example 2     

a = "My"
b = "name is"
c = "Ayesha"
print(a,b,c)


# 15. Output variable example 3

a = "My"
b = "name is"
c = "Ayesha"
print(a + b + c)

# 16. Combine a number and string as variable

a = "Ayesha"
b = 5

print(a,b)

# 17. Golabal variable example 1

a =  "awesome"

def myfunc():
    print("Python is" + x)

myfunc()    

# 18. Golabal variable example 2

a =  "awesome"

def myfunc():
    x = "fantastic"
    print("Python is" + x)

myfunc()

print("Python is" + x)


# 19. Golabal variable example 3

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is" + x)


# 20. Golabal variable example 4

x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is" + x)


