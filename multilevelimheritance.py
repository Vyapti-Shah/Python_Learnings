# Multi-level Inheritance = when a derived class (child class) inherits other derived class (child class)

class Organism:

    alive = True

class Animal(Organism):

    def eat(self):
        print("The animal is eating")

class Dog(Animal):

    def bark(self):
        print("The dog is barking")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()