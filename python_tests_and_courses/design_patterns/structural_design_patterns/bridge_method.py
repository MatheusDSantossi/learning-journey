# Code without using the bridge method. We have a class
# with three attributes named as length, breadth, and height and three methods named as ProduceWithAPI1(), ProduceWithAPI2(),and expand(). Out of these producing methods are implementation-specific as we have two production APIS
print("Code without using the bridge method.")

class Cuboid:
    class ProducingAPI1:
        """Implementation Specific Implementation"""
        def produceCuboid(self, length, breadth, height):
            print(f"Producing cuboid with length: {length}, breadth: {breadth}, height: {height} using API1")
            
    class ProducingAPI2:
        """Implementation Specific Implementation"""
        def produceCuboid(self, length, breadth, height):
            print(f"Producing cuboid with length: {length}, breadth: {breadth}, height: {height} using API2")
    def __init__(self, length, breadth, height):
        """Initialize the necessary attributes"""
        self._length = length
        self._breadth = breadth
        self._height = height
    def produceWithAPI1(self):
        """Implementation specific Abstraction"""
        objectAPIone = self.ProducingAPI1()
        objectAPIone.produceCuboid(self._length, self._breadth, self._height)
        
    def produceWithAPI2(self):
        """Implementation specific Abstraction"""
        objectAPItwo = self.ProducingAPI2()
        objectAPItwo.produceCuboid(self._length, self._breadth, self._height)
        
    def expand(self, times):
        """Implementation independent Abstraction"""
        self._length = self._length * times
        self._breadth = self._breadth * times
        self._height = self._height * times
        
# Instantiate a Cuboid
cuboid1 = Cuboid(1,2,3)

# Draw it using APIone
cuboid1.produceWithAPI1()

# Instantiate another Cuboid
cuboid2 = Cuboid(19, 20, 21)

# Drawing it using APItwo
cuboid2.produceWithAPI2()      

"""Code implemented with Bridge Method.
   We have a Cuboid class having three attributes
   named as length, breadth, and height and three
   methods named as produceWithAPIOne(), produceWithAPItwo(),
   and expand(). Our purpose is to separate out implementation
   specific abstraction from implementation-independent
   abstraction"""
print("Code implemented with Bridge Method.")

class ProducingAPI1:
    """Implementation specific Absctraction"""
    def produceCuboid(self, length, breadth, height):
            print(f"Producing cuboid with length: {length}, breadth: {breadth}, height: {height} using API1")

class ProducingAPI2:
    """Implementation specific Abstraction"""
    def produceCuboid(self, length, breadth, height):
            print(f"Producing cuboid with length: {length}, breadth: {breadth}, height: {height} using API2")

class Cuboid:
    def __init__(self, length, breadth, height, producingAPI):
        """Initialize the necessary attributes Implementation independent Abstraction"""
        self._length = length
        self._breadth = breadth
        self._height = height
        
        self._producingAPI = producingAPI
        
    def produce(self):
        """Implementation specific abstraction"""
        self._producingAPI.produceCuboid(self._length, self._breadth, self._height)
        
    def expand(self, times):
        """Implementation independent Abstraction"""
        self._length = self._length * times
        self._breadth = self._breadth * times
        self._height = self._height * times


"""Instantiate a cuboid and pass to it an
   object of ProducingAPIone"""

cuboid1 = Cuboid(1, 2, 3, ProducingAPI1())
cuboid1.produce()

cuboid2 = Cuboid(19, 19, 19, ProducingAPI2())
cuboid2.produce()

# Usage:
# The bridge Method is always considered as one of the
# best methods to organize the class hierarchy.

# Applicability
# Run-time Binding: Generally Bridge method is used to provide the run-time binding of the implementation, here run-time binding refers to what we can call a method at run-time instead of compile-time.
# Mapping classes: The bridge method is used to map the orthogonal class hierarchies
# UI Environment: A real-life application of the Bridge method is used in the definition of shapes in a UI Environment

