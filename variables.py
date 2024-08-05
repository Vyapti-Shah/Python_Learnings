#variables - a container of a value. Behaves as the value that it contains.
first_name = "Vyapti"
last_name = "Shah"
print("Hello " + first_name)
print(type(first_name))

full_name = first_name + " " + last_name
print(full_name)

age = 19
age += 1
print(age)
print(type(age))
print(str(age) + " years") #for writing an int variable with a string variable we have to convert the int variable to string

cgpa = 8.25
print(cgpa)
print(type(cgpa))
print(str(cgpa) + " marks")

human = True
print(human)
print(type(human))
print("Are you a human: " + str(human))