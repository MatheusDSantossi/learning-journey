"""State class: base state class"""
class State:
    # Base state. This is to share functionality
    def scan(self):
        # Scan the dial to the next station
        self.pos +=1
        
        if self.pos == len(self.stations):
            self.pos = 0
        
        print("Visiting... station is {}{}".format(self.stations[self.pos], self.name))
        
"""Class for AM state of the radio"""
class AmState(State):
    # Constructor for AM state class
    def __init__(self, radio):
        self.radio = radio
        self.name = "AM"
        self.stations = ["101.5", "103.5", "105.5", "107.5", "109.5", "111.5", "113.5", "115.5", "117.5", "119.5"]
        self.pos = 0
        
    def toggle_amfm(self):
        # Toggle AM/FM mode
        self.radio.state = self.radio.fm_state
        print("AM/FM mode toggled to FM")

"""Separate class for FM state"""
class FmState(State):
    # Constructor for FM state
    def __init__(self, radio):
        self.radio = radio
        self.name = "FM"
        self.stations = ["87.5", "89.5", "91.5", "93.5", "95.5", "97.5", "99.5", "101.5", "103.5", "105.5"]
        self.pos = 0
        
    def toggle_amfm(self):
        # Toggle AM/FM mode
        self.radio.state = self.radio.am_state
        print("AM/FM mode toggled to AM")

"""Dedicated Radio class"""

class Radio:
    # A radio. It has a scan button, and an AM / FM toggle switch
    def __init__(self):
        self.am_state = AmState(self)
        self.fm_state = FmState(self)
        self.state = self.am_state
        
    # Method to toggle the switch
    def toggle_amfm(self):
        self.state.toggle_amfm()
        
    # Method to scan
    def scan(self):
        self.state.scan()
        
if __name__ == "__main__":
    # Create a radio
    radio = Radio()
    actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
    actions *= 2
    
    for action in actions:
        action()
    
    # # Scan the radio
    # radio.scan()
    
    # # Toggle AM/FM mode
    # radio.toggle_amfm()
    
    # # Scan the radio again
    # radio.scan()
    
    # # Toggle AM/FM mode again
    # radio.toggle_amfm()
    
    # # Scan the radio one more time
    # radio.scan()
        
"""
Advantages
Open/Closed Principle: We can easily introduce the new states without changing the content of existing states of client’s code.
Single Responsibility Principle: It helps in organizing the code of particular states into the separate classes which helps in making the code feasible for the other developers too.
Improves Cohesion: It also improves the Cohesion since state-specific behaviors are aggregat    ed into the ConcreteState classes, which are placed in one location in the code.
Disadvantages
Making System complex: If a system has only a few number of states, then its not a good choice to use the State Method as you will end up with adding unnecessary code.
Changing states at run-time: State method is used when we need to change the state at run-time by inputting at different sub-classes, this will be considered as a disadvantage as well because we have a clear separate State classes with some logic and from the other hand the number of classes grows up.
Sub-Classes Dependencies: Here the each state derived class is coupled to its sibling, which directly or indirectly introduces the dependencies between sub-classes.
"""
