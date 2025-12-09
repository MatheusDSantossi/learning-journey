import random

class Course_at_CFG:
    """Example of a portal for courses"""
    
    def __init__(self, courses_factory = None):
        """Course factory is out abstract factory"""
        # self.courses_factory = courses_factory if courses_factory else self._default_courses_factory()
        self.courses_factory = courses_factory
        
    def show_course(self):
        """creates and shows courses using the abstract factory"""
        course = self.courses_factory()
        print(f"We have a course named {course}")
        print(f'Its price is {course.Fee()}')
        
class DSA:
    """Class for Data Structure and Algorithms"""
    def Fee(self):
        return 1000
    def __str__(self):
        return "DSA"

class STL:
    """Class for standard Template Library"""
    
    def Fee(self):
        return 8000
    def __str__(self):
        return "STL"

class SDE:
    """Class for Software Development Engineer"""
    
    def Fee(self):
        return 15000
    def __str__(self):
        return "SDE"

def random_course():
    """Randomly selects a course"""
    return random.choice([SDE, STL, DSA])()

if __name__ == "__main__":
    course = Course_at_CFG(random_course)
    
    for i in range(5):
        course.show_course()