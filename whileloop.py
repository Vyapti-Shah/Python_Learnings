#While Loop - a statement that will execute it's block of code, as long as it's condition remains true

# while 1==1:
#     print("I'm stuck in a loop")

name = ""
while len(name) == 0:
    name = input("Enter your name : ")
print("Hello " + name)

age = None
while not age:
    age = input("Enter your age : ")
print("Hello " + str(age))