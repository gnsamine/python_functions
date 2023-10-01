# String Methods

# to list methods use "dir()"

# print(dir(int))
# print(dir(str))

# len method
name = "amine"
a = len(name)
print(a)

print(len("merhaba amine"))
#if a function is defined into a class it becomes a method,
# othervise it is a function
#functions are independent, methodes defined into classes


#upper() and #lower()

x = "amine".upper()
print(x)

y = "NABER".lower()
print(y)

#replace characters 
hi = "hello hello hello"
print(hi.replace("l", "y"))

# split characters
print(hi.split())
print(hi.split("e"))

#strip = Remove spaces at the beginning 
# and at the end of the string

hi2 = "    hello hello hello"
print(hi2.strip())
print(hi2.strip(" h"))
print(hi2.strip(" hel"))

# capitalize = make first word capitalize
a = "foot".capitalize()
print(a) 




