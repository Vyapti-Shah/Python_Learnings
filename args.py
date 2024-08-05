# *args - parameter that will pack all parameters into a tuple
#       - useful so that a function can accept a varying amount of arguements

def add(*stuff):
    sum = 0
    for i in stuff:
        sum += i
    return sum
print(add(1,2,3,4,5,6))

def add_items(*items):
    sum = 0
    items = list(items) #convert the items in form of tuple to the form of lists so that the elements can be changed
    items[1] = 0
    for i in items:
        sum += i
    return sum
print(add_items(1,5,2,3,4))

