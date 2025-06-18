from abc import ABC, abstractmethod
import math

#Build a class hierarchy: e.g., Shape → Circle, Square

class Shape(ABC):
    @abstractmethod
    def area(self):
        #every class whcih inherits from Shape will implement area method
        pass

#Use polymorphism to calculate area/volume
class Circle(Shape):
    def __init__(self, radius): #constructor
        self.radius = radius
    
    def area(self): #override abstract method from shape
        return math.pi * self.radius**2
    


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Cube:
    def __init__(self, side):
        self.side = side

    def volume(self):
        return self.side ** 3


#Add generator-based lazy data processing
#define generator function- takes maybe a list of shapes
def shape_calculator(Shapes):
    for shape in shapes: #loop through each shape
        if hasattr(shape, "area"): #check if shape has area method
            yield f"Area: {shape.area():.2f}" # calls shapes areas method to get a number
        elif hasattr(shape, 'volume'):
            yield f"Volume: {shape.volume():.2f}"

# hasattr() checks if an object supports a method or attribute
#yield produces a value but keeps funtion paused