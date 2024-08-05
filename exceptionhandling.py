# exception - event detected during execution that interrupt the flow of a program 

try:
    numerator = int(input("Enter a number to be divided : "))
    denominator = int(input("Enter a number to divide by : "))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("A number cannot be divided by 0 as it gives a value at infinity!")
except ValueError as e:
    print(e)
    print("You can enter numbers only!")
except Exception as e:
    print(e)
    print("Something went wrong!")
else:
    print(result)
finally:
    print("This will always execute!")