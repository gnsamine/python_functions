#Lists are ordered.
# Lists can contain any arbitrary objects.
# List elements can be accessed by index.
# Lists can be nested to arbitrary depth.
# Lists are mutable.
# Lists are dynamic.

a = ['foo', 'bar', 'baz', 'qux']
print(a)

b = [2, 4, 6, 8]
print(b)

c= [21.42, 'foobar', 3, 4, 'bark', False, 3.14159, b]
print(c)
print(len(c))

print(c[-1])

print(type(c[7]))
print(c[7][1])
print(type(c[7][1])) 

c[1] = 5
print(c)



# append = to add sth into the end of lsit

b.append("100")
print(b)

# pop 

b.pop(0)
print(b)

#insert = add to index
b.insert(1, 33)
print(b)