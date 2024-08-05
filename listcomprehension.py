# list comprehension - a way to create a new list with less syntax
#                    - can mimic certain lambda functions, easier to read
#                    - list = [expression for item in iterable]
#                    - list = [expression for item in iterable if conditional]
#                    - list = [expression if/else for item in iterable]


# list = [expression for item in iterable]
squares = [] # create an empty list
for i in range(1,11): # create a for loop
    squares.append(i * i) # define what each loop iterable should do
print(squares)

square = [i * i for i in range(1,11)]
print(square)


# list = [expression for item in iterable if conditional]
marks = [100,90,80,70,60,50,40,30,20,10,0]
passed_marks = list(filter(lambda x: x>=60, marks))
print(passed_marks)

students = [100,90,80,70,60,50,40,30,20,10,0]
passed_students = [i for i in students if i >= 60]
print(passed_students)


# list = [expression if/else for item in iterable]
students = [100,90,80,70,60,50,40,30,20,10,0]
passed_students = [i if i >= 60 else "Failed" for i in students]
print(passed_students)