# Monostate/Borg Singleton Design Pattern
print("Monostate/Borg Singleton Design Pattern")

# Singleton Borg pattern
class Borg:
    # state shared by each instance
    __shared_state = dict()
    
    # constructor method
    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = "Mathew State"
        
    def __str__(self):
        return self.state
    
# main method
if __name__ == "__main__":
    # creating instance of the objects
    person1 = Borg()
    person2 = Borg()
    person3 = Borg()
    
    person1.state = "Matheus State"
    person2.state = "Matthheww State"
    
    print(person1)
    print(person2)
    
    person3.state = "Geeks"
    print(person1)
    print(person2)
    print(person3)
    
    
# Double Checked Locking singlenton pattern
print("Double Checked Locking singlenton pattern")
import threading

class SingletonDoubleChecked(object):
    # resources shared by each and every instance
    
    __singleton_lock = threading.Lock()
    
    __singleton_instance = None
    
    # define the classmethod
    @classmethod
    def instance(cls):
        # cehck for the singleton instance
        if not cls.__singleton_instance:
            with cls.__singleton_lock:
                # double check
                if not cls.__singleton_instance:
                    cls.__singleton_instance = cls()
        
        # return the singleton instance
        return cls.__singleton_instance

# main method
if __name__ == "__main__":
    # Create class X
    class X(SingletonDoubleChecked):
        pass
    # Create class Y
    class Y(SingletonDoubleChecked):
        pass
    
    A1, A2 = X.instance(), X.instance()
    B1, B2 = Y.instance(), Y.instance()

    print('A1 : ', A1)
    print('A2 : ', A2)
    print('B1 : ', B1)
    print('B2 : ', B2)


# Classic implementation of Singleton Design pattern
print("Classic implementation of Singleton Design pattern")
class Singleton:
    __shared_instance = 'Matheus'
    
    @staticmethod
    def getInstance():
        """Static Access Method"""
        if Singleton.__shared_instance == "Matheus":
            Singleton()
        return Singleton.__shared_instance
    
    def __init__(self):
        """ Virtual private constructor"""
        if Singleton.__shared_instance != "Matheus":
            raise Exception("This class is a singleton class!!")
        else:
            Singleton.__shared_instance = self
        
# Main method
if __name__ == "__main__":
    # Create object of Singleton Class
    obj = Singleton()
    # obj2 = Singleton()
    print(obj)
    # print(obj2)
    
    obj = Singleton.getInstance()
    print(obj)