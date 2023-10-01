#ordered : it means that the items have a defined order, and that order will not change.
#changable: meaning that we can change, add or remove items after the dictionary has been created.
#Dictionaries cannot have two items with the same key


dictt = {'name' :'carl',
        'surname':'sagan',
        'age' : 30,
        'smart':True,
        'childerns': ["em","x","y"]}

print(dictt)
print(dictt["childerns"])

print(dictt["childerns"][0])
print(dictt.get("childerns"))


#key interrogate

print('surname' in dictt)

#value interchange

dictt["childerns"] = ["bmw","mercedes","porsche"]
print(dictt)

#get keys and values seperately
print(dictt.keys())
print(dictt.values())

#to transform list to tuple format

print(dictt.items())

#update mathod adds nwe key-value pairs,
#if there exist one key same as new key it update the older values

dictt.update({"birthdate":"10.12.2002"})
print(dictt)

dictt.update({"birthdate":"10.12.1905"})
print(dictt)