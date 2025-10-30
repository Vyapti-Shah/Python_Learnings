#Generator expressions: with the use of yield keyword only to topmost function is executed and rest are ignored until next() is called
# The number of times next() is called, that many functions are executed
def topten():
    yield 5
    yield 10
    yield 15
    yield 20
values = topten()
print(values.__next__()) 
print(values.__next__()) 

print()

def generate_square():
    n = 1
    while n <= 10:
        yield n * n
        n += 1
square = generate_square()
for i in square:    
    print(i)