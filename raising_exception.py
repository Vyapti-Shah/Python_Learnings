#Raising Exception
a = int(input("Enter a: "))
b = int(input("Enter b: "))
try:
    result = a / b
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Execution completed.")

print()

marks = int(input("Enter your marks: "))
try:
    if marks < 0 or marks > 100:
        raise Exception("Marks should be between 0 and 100.")
    elif marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
except Exception as e: #can use ValueError as ve insted of Exception as e
    print("Error:", e)