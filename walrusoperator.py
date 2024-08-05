# walrus operator [:=] (assignment expression) - assigns values to variables as part of a larger expression
#                                         - new to Python 3.8

#happy = True
#print(happy)

print(happy := True)

foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)

friends = list()
while friend := input("Name your friends: ") != "quit":
    friends.append(friend)