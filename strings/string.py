print("amine")
name = "amine"

print(name)

long_str ="""hahahahhah hahhahahha ahahahhaha
hahahahah
ahhahhahahaha
naber"""
print(long_str)



#reach elements of variables
print(name[0])
print(name[-1])

#Slice thing
"""
Can slice strings using [start:end:step]
If you give two numbers, [start:end], step = 1 by default
"""

poetry = "Mavi, masmavi bir işik / Ortasinda yüzmekteyim..."
print(poetry[:])
print(poetry[:7]) 
print(poetry[7:])
print(poetry[2:7]) 
print(poetry[2::3]) 


#question if the word inside the string

a = "Masmavi" in poetry
print(a)

b = "işik" in poetry
print(b)


#formating strings
salary = 7512.32165
print(f'Your salary is {salary}')

print( f'Your salary is {salary:.2f}')


"""
print(f’Your salary is {salary:m.nf}’)
m: places reserved for value, including decimal point.
n: number of decimal places
f: format specifier for float values

print(f’Your age is {age:md}’)
m: places reserved for value
d: format specifier for int values

print(f‘Your name is {name:ms}’)
m: places reserved for value
s: format specifier for string values

"""

salary = 7510.2685
age = 32
name = 'Jane'
print(f'Name: {name:10s} Age: {age:05d} Salary: {salary:.2f}')


name = "amine"
lastname = "güneş"
age = 98
income = 9898989898.9898989898989898
print(f"{name:s} is a client who is {age:05d} years old and has the income {income:19.5f}")


#repetition
silly = 'hi' + " " + name * 3
print(silly)

#character encoding
"""ord(char) to get numerical code for character char 
chr(num) to get corresponding character for integer num"""

print(ord("A"), ord("a"))
print(chr(5865), chr(67))


# in and not in


print('way' in 'John Wayne')
print('way'.lower() in 'John Wayne'.lower())

print('was' not in 'I am happy')



"""
not a -> True if a is False
         False if a is True
a and b -> True if both are True
           False if either is False
a or b -> True if either or both are True
          False if neither are True
"""
a = 3
b = 5
c = 5

print(not a)
print(a and b) 
print (b and c)
print(a or b),
print(b or c)