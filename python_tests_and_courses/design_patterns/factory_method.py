# Factory method
# Design pattern

class FrenchLocalizer:
    """Returns the french version"""
    
    def __init__(self):
        self.translations = {"car": "voiture", "bike": "bicyclette", "cycle": "cyclette"}
        
    def localize(self, msg):
        """change the message using translations"""
        return self.translations.get(msg, msg)
    
class SpanishLocalizer:
    """Returns the spanish version"""
    
    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta", "cycle": "ciclo"}
        
    def localize(self, msg):
        """change the message using translations"""
        return self.translations.get(msg, msg)

class EnglishLocalizer:
    """Returns the english version"""
    # def __init__(self):
    #     self.translations = {}

    def localize(self, msg):
        return msg
    
def Factory(language="English"):
    """Factory method to return a localizer object"""
    localizers = {
        "French": FrenchLocalizer,
        "Spanish": SpanishLocalizer,
        "English": EnglishLocalizer
    }
   
    return localizers[language]()

if __name__ == "__main__":
    french_localizer = Factory("French")
    spanish_localizer = Factory("Spanish")
    english_localizer = Factory("English")
    
    message = ["car", "bike", "cycle"]
    
    for msg in message:
        print(f"Original: {msg}")
        print(f"French: {french_localizer.localize(msg)}")
        print(f"Spanish: {spanish_localizer.localize(msg)}")
        print(f"English: {english_localizer.localize(msg)}")
        print("---")
