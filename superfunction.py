# super - Function used to give access to the methods of parent class(superclass)
#       - Returns a temporary object of a parent class when used 

class Rectangle:
    def __init__(self,lenght,width):
        self.length = lenght
        self.width = width

class Square(Rectangle):
    def __init__(self,lenght,width):
        super().__init__(lenght,width)
    
    def area(self):
        return self.length*self.width

class Cube(Rectangle):
    def __init__(self,lenght,width,height):
        super().__init__(lenght,width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height
    
square = Square(3,3)
cube = Cube(3,3,3)

print(square.area())
print(cube.volume())