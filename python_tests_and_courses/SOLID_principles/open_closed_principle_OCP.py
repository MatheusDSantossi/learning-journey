# Shape class

from math import pi

class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]
        elif self.shape_type == "circle":
            self.radius = kwargs["radius"]
            
    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return pi * self.radius ** 2
        
rectangle = Shape("rectangle", width=10, height=5)
print(rectangle.calculate_area())

circle = Shape("circle", radius=5)
print(circle.calculate_area())

# NOTE: This class works, you can create circles and rectangles, compute their area, and so on. However, it looks pretty complicated, imagine that you need to add a new shape, maybe a square. How would you do that? Well, one option would be add another elif clause to .__init__() and to .calculate_area(). Having to make these change means that your class is open to modification, which violates the open-closed principle.

# this is a possible solution for the problem

from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        
    @abstractmethod
    def calculate_area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height
        
    def calculate_area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius
        
    def calculate_area(self):
        return pi * self.radius**2
    
class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def calculate_area(self):
        return self.side ** 2
