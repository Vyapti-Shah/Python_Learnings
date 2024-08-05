#keyword arguements - arguements preceded by an identifier when we pass them to a function
#                   - The order of the arguements doesn't matter, unlike positional arguements
#                   - Python knows the name of the arguements that our functions receives

def hello(first,middle,last):
    print("Hello " + first + " " + middle + " " + last) 

hello("Vyapti","Sanjay","Shah")
hello(last="Shah",first="Sanjay",middle="Jayantilal")