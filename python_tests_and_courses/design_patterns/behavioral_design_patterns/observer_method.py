# Let’s discuss the solution to the above-described problem. Here comes the object Subject into the limelight. But it also notifies the other objects also that’s why we generally call it Publisher. All the objects that want to track changes in the publisher’s state are called subscribers.

class Subject:
    """Represents what is being observed"""
    def __init__(self):
        """Create an empty observer list"""
        self._observers = []
        
    def notify(self, modifier = None):
        """Alert the observers"""
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)
    
    def attach(self, observer):
        """If the observer is not in the list append it into the list"""
        if observer not in self._observers:
            self._observers.append(observer)
            
    def detach(self, observer):
        """Remove the observer from the observer list"""
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
        
class Data(Subject):
    """Monitor the object"""
    def __init__(self, name=""):
        Subject.__init__(self)
        self.name = name
        self._data = 0
        
    @property
    def data(self):
        return self._data
        
    @data.setter
    def data(self, value):
        self._data = value
        self.notify()
    
class HexViewer:
    """Updates the HexViewer"""
    def update(self, subject):
        print("HexViewer: Subject {} has data 0x{:x}".format(subject.name, subject.data))
        
class OctalViewer:
    """Updates the Octal viewer"""
    def update(self, subject):
        print("OctalViewer: subject " + str(subject.name) + " has data " + str(oct(subject.data)))

class DecimalViewer:
    """Updates the decimal viewer"""
    def update(self, subject):
        print("DecimalViewer: subject % s has data % d" % (subject.name, subject.data))


if __name__ == "__main__":
    
    """provide the data"""
    obj1 = Data('Data 1')
    obj2 = Data('Data 2')

    view1 = DecimalViewer()
    view2 = HexViewer()
    view3 = OctalViewer()

    obj1.attach(view1)
    obj1.attach(view2)
    obj1.attach(view3)

    obj2.attach(view1)
    obj2.attach(view2)
    obj2.attach(view3)

    obj1.data = 10
    obj2.data = 15

# Disadvantages

# Memory Leakage: Memory leaks caused by Lapsed Listener Problem because of explicit register and unregistering of observers.
# Random Notifications: All the subscribers present gets notification in the random order.
# Risky Implementations: If the pattern is not implemented carefully, there are huge chances that you will end up with large complexity code.

# Applicability

# Multi-Dependency: We should use this pattern when multiple objects are dependent on the state of one object as it provides a neat and well tested design for the same.
# Getting Notifications: It is used in social media, RSS feeds, email subscription in which you have the option to follow or subscribe and you receive latest notification.
# Reflections of Object: When we do not coupled the objects tightly, then the change of a state in one object must be reflected in another object.
