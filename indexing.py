#index operator [] - gives access to a sequence's element (str,list,tuples)

name = "vyapTi ShAH"

if(name[0].islower()):
    name = name.capitalize()
print(name)

first_name = name[:6].upper()
last_name = name[7:].upper()
last_character = name[-1]
secondlast_character = name[-2]

print(first_name)
print(last_name)
print(last_character)
print(secondlast_character)