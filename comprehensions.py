#Comprehensions - compact ways to create lists, sets, dictionaries (and generator expressions). 
#               - They’re usually faster and more readable than manual loops.

# list comprehension
squares = [x*x for x in range(6)]  # [0,1,4,9,16,25]

# with condition
evens = [x for x in range(10) if x % 2 == 0]

# set comprehension (unique)
unique_lengths = {len(s) for s in ["a","ab","abc","a"]}

# dict comprehension
names = ["a","b"]
ages = [20, 25]
d = {n: a for n, a in zip(names, ages)}  # {'a':20, 'b':25}

# nested comprehension: flatten list of lists
matrix = [[1,2], [3,4]]
flat = [x for row in matrix for x in row]  # [1,2,3,4]
