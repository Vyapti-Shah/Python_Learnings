from car import Car

car_1 = Car("BMW","M4","2023","black")
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.colour)

print()

car_2 = Car("Mecedes","Benz-C class","2024","grey")
print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.colour)

print()

print(car_1.wheels)
print(car_2.wheels)

print()

print(Car.wheels)