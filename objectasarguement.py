# object as arguement 

class Car:
    colour = None

class Motorcycle:
    colour = None

def change_colour(vehicle,colour):
    vehicle.colour = colour

car_1 = Car()
car_2 = Car()
car_3 = Car()
bike_1 = Motorcycle()
bike_2 = Motorcycle()

change_colour(car_1,"black")
change_colour(car_2,"grey")
change_colour(car_3,"lightblue")
change_colour(bike_1,"red")
change_colour(bike_2,"blue")

print(car_1.colour)
print(car_2.colour)
print(car_3.colour)
print(bike_1.colour)
print(bike_2.colour)