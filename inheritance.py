class Animal:

    alive = True

    def eat(self):
        print("The animal is eating")

    def sleep(self):
        print("The animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("The rabbit is running")

class Fish(Animal):
    def swim(self):
        print("The fish is swimming")

class Pigeon(Animal):
    def fly(self):
        print("The pigeon is flying")

rabbit = Rabbit() #object
fish = Fish() #object
pigeon = Pigeon() #object

print(rabbit.alive)
fish.eat()
pigeon.sleep()

print()

rabbit.run()
fish.swim()
pigeon.fly()