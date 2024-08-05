#functions - a block of code which is executed only when it is called
# def = define a function

def hello():
    print("Hello!")
    print("Have a nice day!")

hello()
hello()

print()

def helloName(name):
    print("Hello " + name)
    print("Have a nice day!")

helloName("Vyapti")
helloName("You")

print()

my_name = "V S"
helloName(my_name)

print()

def helloName(name):
    print("Hello " + name)
    print("Have a nice day!")

helloName("Vyapti")
helloName("You")

print()

def helloName(first_name,last_name,age):
    print("Hello " + first_name + " " + last_name)
    print("You are " + str(age) + " years old")
    print("Have a nice day!")

helloName("Vyapti","Shah",19)