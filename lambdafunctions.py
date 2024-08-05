# lambda functions - functions written in 1 line using lambda keyword
#                  - accepts any number of arguements, but only has one expression
#                  - it is a shortcut
#                  - useful if needed for a shot period of time, throw away
#          formula - lambda parameters:expression 

def double(x):
    return x * 2
print(double(5))

square = lambda y : pow(y,2)
print(square(5))
multiply = lambda x,y : x * y
print(multiply(5,6))
add = lambda x,y,z : x + y + z
print(add(2,8,5))
full_name = lambda firstname,lastname : firstname + " " + lastname
print("Vyapti","Shah")
age_check = lambda age:True if age >= 18 else False
print(age_check(15))
print(age_check(18))