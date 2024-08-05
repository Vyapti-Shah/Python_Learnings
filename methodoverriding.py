#Method Overriding - ability of an OOP language to allow a subclass(child class) to provide a specific implementation of a method 
#                    that is already provided in the superclass(parent class)

class Animal:

    def eat(self):
        print("The animal is eating")

class Rabbit(Animal):
    def eat(self):
        print("The rabbit is eating a carrot") #overrides the method of the superclass
        #return super().eat() #output of super(parent) class

rabbit = Rabbit()
rabbit.eat()