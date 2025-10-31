#Polymorphism: the ability of different objects to be accessed through the same interface, each providing its own independent implementation of that interface.
#            : One thing existing in many forms 

class Dog:
    def speak(self):
        return "Woof!"
class Cat:
    def speak(self):
        return "Meow!"
class Cow:
    def speak(self):
        return "Moo!"
def animal_sound(animal):
    print(animal.speak())   
dog = Dog()
cat = Cat()
cow = Cow()
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
animal_sound(cow)  # Output: Moo!
print()

#Polymorphism with Inheritance
class Bird:
    def speak(self):
        return "Chirp!"
class Parrot(Bird):
    def speak(self):
        return "Squawk!"
class Sparrow(Bird):
    def speak(self):
        return "Tweet!"
def bird_sound(bird):
    print(bird.speak())
parrot = Parrot()
sparrow = Sparrow()
bird_sound(parrot)  # Output: Squawk!
bird_sound(sparrow)  # Output: Tweet!
print()

#Polymorphism with Built-in Functions
numbers = [1, 2, 3, 4, 5]
print("Using len() function:")
print(len(numbers))  # Output: 5
text = "Hello, World!"
print("Using len() function on string:")
print(len(text))  # Output: 13
print()

#Polymorphism with Operators
print("Using + operator:")
print(5 + 10)          # Output: 15 (integer addition)
print("Using + operator with strings:")
print("Hello, " + "World!")  # Output: Hello, World! (string concatenation)
print("Using * operator:")  
print(3 * 4)          # Output: 12 (integer multiplication)
print("Using * operator with strings:")
print("Hi! " * 3)     # Output: Hi! Hi! Hi! (string repetition)