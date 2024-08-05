# duck typing - concept ehere the class of an object is less important than the methods/attribute
#             - class type is not checked if minimum methods/attributes are present
#             - "if it walks like a duck, and it quacks liike a duck, then must be a duck"

class Duck:
    def walk(self):
        print("The duck is walking")
    def talk(self):
        print("The duck is quacking")

class Chick:
    def walk(self):
        print("The chick is walking")
    def talk(self):
        print("The chick is clucking")

class Person():
    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("You caught the critter")

duck = Duck()
chick = Chick()
person = Person()

person.catch(duck)
person.catch(chick) #as the methods and attributes inside the duck and chick class are same it will print the chick method 
                    #without calling it on itself and print the respective output