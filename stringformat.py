# str.format() - optional method that gives users more control when displaying output

print("Inky Pinky Ponky")

name = "farmer"
animal = "donkey"
print("A " + name + " had a " + animal)

print()

print("The {} died {} cried ".format("donkey","farmer"))

print()

print("The {} died {} cried ".format(animal,name)) 

print()

print("The {1} died {0} cried ".format(animal,name)) # positional arguement

print()

print("The {1} died {1} cried ".format(animal,name)) # positional arguement

print()

print("The {name} died {animal} cried ".format(animal="donkey",name="farmer")) # keyword arguement

print()

print("Inky Pinky Ponky")

print()

text = "A {} had a {}"
print(text.format(name,animal))

print()

my_name = "Vyapti"
print("Hello, my name is {}. Nice to meet you".format(my_name))
print("Hello, my name is {:10}. Nice to meet you".format(my_name)) #10 spaces randomly
print("Hello, my name is {:<10}. Nice to meet you".format(my_name)) #left align
print("Hello, my name is {:>10}. Nice to meet you".format(my_name)) #right align
print("Hello, my name is {:^10}. Nice to meet you".format(my_name)) #centre align

print()

number = 3.14159
print("The number pi is {}".format(number))
print("The number pi = {:.2f}".format(number))
print("pi = {:.3f}".format(number))

print()

num = 1000000
print("The number is {}".format(num))
print("The number = {:,}".format(num))
print("The number is {:b}".format(num)) #converts to binary number
print("The number is {:o}".format(num)) # converts to octal number
print("The number is {:x}".format(num)) #converts to lowercase hexadecimal number
print("The number is {:X}".format(num)) #converts to uppercase hexadecimal number
print("The number is {:e}".format(num)) #converts to lowercase scientific notation
print("The number is {:E}".format(num)) #converts to uppercase scientific notation