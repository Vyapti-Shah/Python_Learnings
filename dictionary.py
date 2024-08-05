# Dictionary - A changeable, unordered collection of unique key:value parts
#            - Fast because they use hashing, allows us to access a value quickly

capitals = {'Inia':'New Delhi',
            'USA':'Washington DC',
            'China':'Beijing',
            'Russia':'Moscow'}
print(capitals['Russia'])
print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

print()

for key,value in capitals.items():
    print(key,value)

print()

capitals.update({'Germany':'Berlin'})
for key1,value1 in capitals.items():
    print(key1,value1)

print()

capitals.update({'USA':'Las Vegas'})
for key2,value2 in capitals.items():
    print(key2,value2)

print()

capitals.pop('China')
for key3,value3 in capitals.items():
    print(key3,value3)  

print()

capitals.clear()
for key4,value4 in capitals.items():
    print(key4,value4) 