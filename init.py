#when there are two variables where did you get them from? therefore we use a special method which is available in class called __init__ method
# __init__ method is a constructor which is automatically called when an object of the class is created
# special variable is __name__ and special method is __init__
class Computer:
    def __init__(self, cpu, ram): #__init__ method with parameters cpu and ram
        self.cpu = cpu  #assigning the parameter cpu to the instance variable self.cpu
        self.ram = ram  #assigning the parameter ram to the instance variable self.ram

    def config(self):
        print("Configuration is:", self.cpu, self.ram)

#In config method we need to call config but in init it is automatically called when the object is created 
com1 = Computer('i5', 16) #Creating an object com1 of class Computer and passing values for cpu and ram
com2 = Computer('Ryzen 5', 8) #Creating another object com2
com1.config() #Calling the config method for com1
com2.config() #Calling the config method for com2