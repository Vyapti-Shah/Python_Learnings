#Lists - used to store multiple items in a single variable 

fruits = ["apple", "banana", "plum", "cherry"]

print(fruits)

print()

print(fruits[0])

print()

print(fruits[1])

print()

print(fruits[2])

print()

for x in fruits:
    print(x)
    
print()

fruits[1] = "pear"
print(fruits[1])

print()

fruits.append("watermelon")
for y in fruits:
    print(y)

print()

fruits.remove("plum")
for z in fruits:
    print(z)

print()

fruits.pop() #removes the last element
for a in fruits:
    print(a)

print()

fruits.insert(1,"mango")
for b in fruits:
    print(b)

print()

fruits.sort() #sorts elements in alphabetical order
for c in fruits:
    print(c)

print()

fruits.clear() #clears everything
for d in fruits:
    print(d)

print()