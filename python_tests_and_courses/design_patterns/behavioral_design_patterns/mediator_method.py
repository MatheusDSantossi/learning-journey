class Course(object):
    """Mediator class"""
    def displayCourse(self, user, course_name):
        print("[{}'s course]: {}".format(user, course_name))
        
class User(object):
    """A class whose instances want to interact with each other"""
    
    def __init__(self, name):
        self.name = name
        self.course = Course()
        
    def sendCourse(self, course_name):
        self.course.displayCourse(self.name, course_name)
        
    def __str__(self):
        return self.name

# Main method

if __name__ == "__main__":
    user1 = User("John Doe")
    user2 = User("Jane Smith")

    user1.sendCourse("Python Programming")
    user2.sendCourse("Java Programming")

# Disadvantages
# Centralization: It completely centralizes the control because the mediator pattern trades complexity of interaction for complexity in the mediator.
# God Object: A Mediator can be converted into a God Object (an object that knows too much or does too much).
# Increased Complexity: The structure of the mediator object may become too much complex if we put too much logic inside it.

# Applicability
# Reduce the number of sub-classes: When you have realized that you have created a lot of unnecessary sub-classes, then it is preferred to use the Mediator method to avoid these unnecessary sub-classes.
# Air Traffic Controller: Air traffic controller is a great example of a mediator pattern where the airport control room works as a mediator for communication between different flights.
