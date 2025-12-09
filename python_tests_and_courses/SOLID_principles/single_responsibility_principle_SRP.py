# File manager class

from pathlib import Path
from zipfile import ZipFile

# This class violates the single-responsibility principle cause has two reasons for changing its internal implementation, first the read and wirte part and compress and decompress part.
class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)
        
    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)
    
    def write(self, content, encoding="utf-8"):
        self.path.write_text(content, encoding)
        
    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(str(self.path))
    
    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()
            
# Correct implementation

class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)
        
    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)
    
    def write(self, content, encoding="utf-8"):
        self.path.write_text(content, encoding)
        
class ZipFileManager:
    def __init__(self, filename):
        self.path = Path(filename)
        
    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(str(self.path))
            
    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()
