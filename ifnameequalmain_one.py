# if __name__ == '__main__'

# why tho?
# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules

# Python interpreter sets "special variables", one of which is __name__
# then Python will execute the code found within __main__
# Python will assign __name__ variable a value of '__main__' if it's the initial module being run
def hello():
    print("Hello")

if __name__ == '__main__':
    hello()
    print("running this module directly")
else:
    print("running other module infirectly")