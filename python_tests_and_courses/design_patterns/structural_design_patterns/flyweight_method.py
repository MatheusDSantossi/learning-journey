# Flyweight method is a Structural Design Pattern that 
# focus on minimizing the number of objects that are
# required by the program at the run-time. Basically, 
# it creates a Flyweight object which is shared by 
# multiple contexts. It is created in such a fashion 
# that you can not distinguish between an object and a 
# Flyweight Object. One important feature of flyweight 
# objects is that they are immutable. This means that 
# they cannot be modified once they have been constructed.

class ComplexCars(object):
    """Separate class for Complex Cars"""
    def __init__(self):
        pass
    
    def cars(self, car_name):
        return "ComplexPattern[% s]" % (car_name)
    
class CarFamilies(object):
    """dictionary to store ids of the car"""
    car_family = {}
    
    def __new__(cls, name, car_family_id):
        try:
            id = cls.car_family[car_family_id]
        except KeyError:
            id = object.__new__(cls)
            cls.car_family[car_family_id] = id
        return id
    
    def set_car_info(self, car_info):
        """set the car information"""
        cg = ComplexCars()
        self.car_info = cg.cars(car_info)
        
    def get_car_info(self):
        """return the car information"""
        return (self.car_info)
    
if __name__ == "__main__":
    car_data = (('a', 1, 'Audi'), ('a', 2, 'Ferrari'), ('b', 1, 'Audi'))
    car_family_objects = []
    for i in car_data:
        obj = CarFamilies(i[0], i[1])
        obj.set_car_info(i[2])
        car_family_objects.append(obj)
        
    """Similar id's say that they are same objects"""
    
    for i in car_family_objects:
        print("id = " + str(id(i)))
        print(i.get_car_info())

# Applicability

# To Reduce the number of Objects: Generally, Flyweight method is used when our application has a lot of heavy weight objects, to solve this problem we use Flyweight method to get rid of unnecessary memory consumption.
# Object independent Applications: When our application if independent of the object created, then we can make use of this method inorder to save lot of machine space.
# Project Cost Reduction: When it is required to reduce the cost of project in terms of space and time complexity, it is always preferred to use the Flyweight method.

# Advantages 

# Reduced use of RAM: when we have a lot of similar objects present in our application, its always better to use Flyweight method inorder to save a lot of space in RAM
# Improved Data Caching: When the need of client or user is High response time, it is always preferred to use Flyweight method because it helps in improving the Data Caching.
# Improved performance: It ultimately leads to improve in performance because we are using less number of heavy objects.

# Disadvantages

# Breaking Encapsulation: Whenever we try to move the state outside the object, we do breaking of encapsulation and may become less efficient then keeping the state inside the object.
# Hard to handle: Usage of Flyweight method depends upon the language we use, easy to use in language like Python, Java where all object variables are references but typical to use in language like C, C++ where objects can be allocated as local variables on the stack and destroyed as a result of programmer action.
# Complicated Code: Using Flyweight method always increases the complexity of the code to understand for the new developers.
