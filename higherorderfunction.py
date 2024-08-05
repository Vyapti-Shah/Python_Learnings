# higher order function - a. function that either: 1. accepts a function as an arguement 
#                                                  2. returns a function (In puthon, function are also treated as object)

def loud(text):
    return text.upper()
def quite(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quite)

print()

def divisor(x): # divisor is higher order function as it returns dividend function
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(10))