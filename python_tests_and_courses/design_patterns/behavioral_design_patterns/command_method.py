from abc import ABC, abstractmethod

class Command (ABC):
    """Constructor method"""
    def __init__(self, receiver):
        self.receiver = receiver
        
    """Process method"""
    def process(self):
        pass
    
"""Class dedicated to command implementation"""
class CommandImplementation(Command):
    """constructor method"""
    def __init__(self, receiver):
        self.receiver = receiver
        
    """Process method"""
    def process(self):
        self.receiver.perform_action()
        
"""Class dedicated to Receiver"""
class Receiver:
    """Perform action method"""
    def perform_action(self):
        print("Receiver's action")

"""Class dedicated to Invoker"""
class Invoker:
    """command method"""
    def command(self, command):
        self.command = command
        
    """Execute method"""
    def execute(self):
        self.command.process()
        
"""Main method"""
if __name__ == "__main__":
    # Create receiver
    receiver = Receiver()
    
    # Create command
    cmd = CommandImplementation(receiver)
    invoker = Invoker()
    invoker.command(cmd)
    invoker.execute()

# Advantages 
# Open/Closed Principle: We can introduce the new commands into the application without breaking the existing client’s code.
# Single Responsibility Principle: It’s really easy to decouple the classes here that invoke operations from other classes.
# Implementable UNDO/REDO: It’s possible to implement the functionalities of UNDO/REDO with the help of Command method.
# Encapsulation: It helps in encapsulating all the information needed to perform an action or an event.

# Disadvantages
# There are the same disadvantages as the other ones complexity of code and quantity of classes increases.
# Concrete Command: Every individual command is a ConcreteCommand class that increases the volume of the classes for implementation and maintenance.

# Applicability 
# Implementing Reversible operations: As the Command method provides the functionalities for UNDO/REDO operations, we can possibly reverse the operations.
# Parameterization: It’s always preferred to use Command method when we have to parameterize the objects with the operations.
