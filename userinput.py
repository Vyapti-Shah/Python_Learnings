#User Input 

name = input("What is your name? : ")  #user input is always of the string data type
print("Hello " + name)

age = int(input("How old are you? : "))
age = age + 1   # or-> age = int(age) + 1
print("Happy Birthday! You are " + str(age) + " years old now")

height = float(input("How tall are you? : "))
print("You are " + str(height) + "cm tall")