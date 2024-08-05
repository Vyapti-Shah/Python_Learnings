#variable scope - The region where a variable is recognized
#               - A variable is only available from inside the region it is created
#               - A global and locally scoped version of a variable can be created 

name = "Vyapti" #global scope (it is availabe both inside and outside of functions)
middle = "Sanjay"  #global scope (it is availabe both inside and outside of functions)

def display_name():
    name = "Shah"  # local scope (it is availabe only inside of this function)
    print(middle)  # this runs the output of the global variable (as global variable is available inside the function)
    print(name)

print(name)  #this runs the output of the global variable (as global variable is also available outside the function)
display_name()

# Python uses a LEGB rule to use the local variable first then and enclosed variable then global variable and then any other built in variable
# Order of - L = Local
#            E = Enclosing
#            G = Global
#            B = Built-in