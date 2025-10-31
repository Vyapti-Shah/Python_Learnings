#Class and Object
class Computer: #Creating a class named Computer
    def config(self):
        print("I5, 16GB, 1TB")

a= '5'
com1 = Computer() #Creating an object com1 of class Computer where Computer() is a constructor
print("Type of com1 is:", type(com1))

x = 5
print("Type of x is:", type(x))

com2 = Computer() #Creating another object com2 of class Computer

com1.config() #need to call the method config using the object com1 The config takes com1 as an implicit argument
Computer.config(com1) #Another way to call the method config by passing the object com1 as an argument
Computer.config(com2)