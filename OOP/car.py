#Object Oriented Programming
class Car:

    def __init__(self,make,model,year,colour): #constructor=__init__
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour

    def drive(self):
        print("The car "+ self.model + " is driving")

    def stop(self):
        print("The car " + self.model + " has stopped")