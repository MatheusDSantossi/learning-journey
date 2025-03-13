# The Memento Design Pattern is a behavioral design pattern used in software development to capture and externalize an object’s internal state so that it can be restored later without violating encapsulation. The Memento pattern is useful for implementing features like undo/redo operations, state persistence, and checkpoints in applications, allowing the system to revert to a previous state when needed.

class Originator:
    def __init__(self, text):
        self.text = text
        
    def set_text(self, text):
        self.text = text
        
    def create_memento(self):
        return Memento(self.text)
    
    def restore_from_memento(self, memento):
        self.text = memento.get_state()
    
    def __str__(self):
        return self.text
    
class Memento:
    def __init__(self, state):
        self._state = state
        
    def get_state(self):
        return self._state
    
class Caretaker:
    def __init__(self):
        self._mementos = []
        self._current_index = -1
        
    def save(self, memento):
        # Remove future states if any
        if self._current_index + 1 < len(self._mementos):
            self._mementos = self._mementos[:self._current_index + 1]
            
        self._mementos.append(memento)
        self._current_index += 1
        
    def undo(self):
        if self._current_index > 0:
            self._current_index -= 1
            return self._mementos[self._current_index]
        return None
    
    def redo(self):
        if self._current_index + 1 < len(self._mementos):
            self._current_index += 1
            return self._mementos[self._current_index]
        return None

# Example usage
if __name__ == "__main__":
    # Create an Originator (Text Editor)
    editor = Originator("Matheus's Initial Text")

    # Create a Caretaker
    caretaker = Caretaker()

    # Save the initial state
    caretaker.save(editor.create_memento())

    # Make changes and save the state
    editor.set_text("First Edit")
    caretaker.save(editor.create_memento())

    editor.set_text("Second Edit")
    caretaker.save(editor.create_memento())

    # Perform undo operations
    print("Current State:", editor)  # Output: "Second Edit"
    memento = caretaker.undo()
    if memento:
        editor.restore_from_memento(memento)
    print("After Undo:", editor)  # Output: "First Edit"

    # Perform redo operations
    memento = caretaker.redo()
    if memento:
        editor.restore_from_memento(memento)
    print("After Redo:", editor)  # Output: "Second Edit"


"""
When to use Memento Method Design Pattern in Python?
The Memento Design Pattern is particularly useful in scenarios where you need to capture and restore the state of an object without exposing its internal details. Here’s when you should consider using the Memento Pattern:

Undo/Redo Functionality:
Use Case: When implementing features like undo and redo in applications such as text editors or graphic design tools.
Example: A text editor where users need to revert to previous versions of their document or redo actions that were undone.
Snapshot Management:
Use Case: When you need to save and restore the state of an object at specific points in time, allowing for historical states to be revisited.
Example: A game where you want to save the state of the game (e.g., player position, scores) at various checkpoints.
State Preservation Across Transactions:
Use Case: When you need to preserve the state of an object across multiple transactions or operations, ensuring that the state can be recovered if necessary.
Example: An online shopping cart that allows users to revert to a previous state if they navigate away from the cart and come back later.
Encapsulation of State Management:
Use Case: When you want to encapsulate the state management of an object to avoid exposing its internal details and ensure that the state management is handled in a controlled manner.
Example: A drawing application where the state of the canvas (e.g., drawings, colors) needs to be managed without exposing the internal structure of the drawing objects.
Temporary State Storage:
Use Case: When you need to temporarily store the state of an object for a specific duration and restore it later without affecting the main object’s state.
Example: A configuration management system where temporary configurations can be saved and restored as needed.
When not to use Memento Method Design Pattern in Python?
The Memento Method Design Pattern, while useful in many scenarios, is not always the best choice. Here are situations where you might want to avoid using the Memento Pattern:

Simple State Management:
Reason: If the state of the object is simple and does not require frequent saving or restoration, the overhead of implementing the Memento Pattern might be unnecessary.
Example: A basic configuration object with a few properties that rarely changes.
High Memory Usage:
Reason: The Memento Pattern involves storing multiple snapshots of an object’s state, which can lead to high memory consumption, especially if the object state is large or changes frequently.
Example: An application that needs to maintain a large number of states (e.g., a complex graphics editor with numerous large images).
Frequent State Changes:
Reason: If the state of the object changes very frequently, managing and storing all those states can become impractical and inefficient.
Example: A real-time gaming system where the state changes rapidly and requires constant updates.
No Need for State Restoration:
Reason: If there is no requirement for restoring previous states and you don’t need undo/redo functionality, the Memento Pattern may not be necessary.
Example: A system where only the current state is relevant, and historical states are not needed.
Security Concerns:
Reason: If the state contains sensitive information, storing multiple snapshots of the state might pose security risks.
Example: An application that deals with sensitive user data where storing multiple states might expose private information.
"""
