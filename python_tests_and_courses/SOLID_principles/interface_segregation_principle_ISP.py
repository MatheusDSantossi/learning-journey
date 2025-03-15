# Printer class

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass
    
    def fax(self, document):
        pass
    
    def scan(self, document):
        pass
    
class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")
    def fax(self, document):
        raise NotImplementedError("Fax functionality not supported")
    def scan(self, document):
        raise NotImplementedError("Scan functionality not supported")
    
class ModernPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in color...")
    def fax(self, document):
        print(f"Faxing {document}...")
    def scan(self, document):
        print(f"Scanning {document}...")
    

# This implementaion violates the ISP becuase it forces OldPrinter to expose an interface that the class doesn't emplement or need. To fix this issue, you should separate the interface into smaller and more specific classes. Then you can create concrete classes by inheriting from multiple interface classes as needed

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass
    
class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass
    
class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

class NewPrinter(Printer, Fax, Scanner):
    def print(self, document):
        print(f"Printing {document} in color...")
    def fax(self, document):
        print(f"Faxing {document}...")
    def scan(self, document):
        print(f"Scanning {document}...")
