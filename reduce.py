# reduce() - apply a function to an iterable and reduce it to a single cumulative value
#          - performs function on first two elements and repeats process until 1 value remains
# formula = reduce(function,iterable)

import functools

letters = ["V","Y","A","P","T","I"]
word = functools.reduce(lambda x,y: x + y,letters)
print(word)

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x,y: x * y,factorial)
print(result)