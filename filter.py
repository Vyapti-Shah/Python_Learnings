# filter - creates a collection from an iterable for which a function returns true
# formula = filter(function,iterable)
friends = [("Vyapti",19),
           ("Sejal",20),
           ("Sanjay",21),
           ("Jiya",15),
           ("Jinit",10)]

age = lambda data: data[1] >= 18
buddies = list(filter(age, friends))
for i in buddies:
    print(i)