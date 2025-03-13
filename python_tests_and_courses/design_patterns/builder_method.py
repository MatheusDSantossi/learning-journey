# TODO: Review this design pattern because I didn't understand this example.

# Abstract course
class Course:
    def __init__(self):
        self.Fee()
        self.available_batches()
        
    def Fee(self):
        raise NotImplementedError
    
    def __repr__(self):
        return 'Fee : {0.fee} | Batches Available: {0.batches}'.format(self)

# Concrete course
class DSA(Course):
    def Fee(self):
        self.fee = 8000
        
    def available_batches(self):
        self.batches = 2
    
    def __str__(self):
        return "DSA"

# Concrete course
class SDE(Course):
    def Fee(self):
        self.fee = 10000
    
    def available_batches(self):
        self.batches = 4
        
    def __str__(self):
        return "SDE"
    
# Concrete course
class STL(Course):
    def Fee(self):
        self.fee = 5000
        
    def available_batches(self):
        self.batches = 7
        
    def __str__(self):
        return "STL"
    
# Complex course
class ComplexCourse:
    def __repr__(self):
        return 'Fee: {0.fee} | available_batches: {0.batches}'.format(self)
    
# Complex course
class Complexcourse(ComplexCourse):
    def Fee(self):
        self.fee = 7000
        
    def available_batches(self):
        self.batches = 6
    
def construct_course(cls):
    course = cls()
    course.Fee()
    course.available_batches()
    
    return course # return the course object

if __name__ == "__main__":
    dsa = DSA()
    sde = SDE()
    stl = STL()
    
    complex_course = construct_course(Complexcourse)
    print(complex_course)
    
    dsa_course = construct_course(DSA(dsa))
    print(dsa_course)
    