# Decorator method
class WrittenText:
    """Represents a Written text"""
    def __init__(self, text):
        self._text = text
    
    def render(self):
        return self._text
    
class UnderlineWrapper(WrittenText):
    """Wraps a tag in"""
    def __init__(self, wrapped):
        self._wrapped = wrapped
        
    def render(self):
        return f"<u>{self._wrapped.render()}</u>"

class ItalicWrapper(WrittenText):
    """Wraps a tag in"""
    
    def __init__(self, wrapped):
        self._wrapped = wrapped
        
    def render(self):
        return f"<i>{self._wrapped.render()}</i>"

class BoldWrapper(WrittenText):
    """Wraps a tag in"""
    
    def __init__(self, wrapped):
        self._wrapped = wrapped
        
    def render(self):
        return f"<b>{self._wrapped.render()}</b>"

if __name__ == "__main__":
    before_gfg = WrittenText("Matheus")
    after_gfg = ItalicWrapper(UnderlineWrapper(BoldWrapper(before_gfg)))
    
    print("Before: ", before_gfg.render())
    print("After: ", after_gfg.render())

# Applicability

# Incapable Inheritance: Generally, Decorator method is used when it is not possible to extend the behavior of an object using the Inheritance.
# Runtime Assignment: One of the most important feature of Decorator method is to assign different and unique behaviors to the object at the Runtime.
