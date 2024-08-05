# Method Chaining - calling multiple methods sequentially 
#                 - each call performs an action on the same object and returns self 

class Car:
    def turn_on(self):
        print("You started the engine")
        return self    #for using method chaining we have to return 'self' after each method in the class 
    def drive(self):
        print("You are driving the car")
        return self   #for using method chaining we have to return 'self' after each method in the class 
    def brakes(self):
        print("You applied brakes")
        return self   #for using method chaining we have to return 'self' after each method in the class 
    def turn_off(self):
        print("You turned the engine off")
        return self   #for using method chaining we have to return 'self' after each method in the class 

car = Car()

car.turn_on()
car.drive()

print()

car.turn_on().drive().brakes().turn_off()

print()

car.turn_on()\
   .drive()\
   .brakes()\
   .turn_off()