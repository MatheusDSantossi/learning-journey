# Rectangle class

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def calculate_area(self):
        return self.width * self.height
    

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        
    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in ("width", "height"):
            self.__dict__["width"] = value
            self.__dict__["height"] = value
            
square = Square(5)
print(vars(square))

square.width = 7
print(vars(square))
square.height = 9
print(vars(square))

# We've ensured that the Square object always remains a valid square, making easier for the small price of a bit of wasted memory. But this code violates the Liskov substitution principle because you can't replace instances of Rectangle with their Square counterparts.

# THE CORRECT WAY TO DO THIS

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def calculate_area(self):
        return self.width * self.height
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def calculate_area(self):
        return self.side ** 2

def get_total_area(shapes):
    return sum(shape.calculate_area() for shape in shapes)

print(get_total_area([Rectangle(10, 5), Square(5)]))

