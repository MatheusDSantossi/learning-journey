# FrontEnd class

class FrontEnd:
    def __init__(self, back_end):
        self.back_end = back_end
        
    def display_data(self):
        data = self.back_end.get_data_from_database()
        print("Display data: ", data)
        
class BackEnd:
    def get_data_from_database(self):
        return "Data from the database..."
        
# In this example we can lead to scalability issues. For instance, say that your app is growing fast, and you want the app to be able to read data from a REST API. You may think of adding a new method to BackEnd to retireve the data from the REST API. However, that will also require you to modify FrontEnd, which should be closde to modification, accortind to OCP

# To fix the issue, we can apply the dependency inversion principle and make the classes depend on abstractions rather than on concrete implementations like BackEnd. In the example below, we can introduce a DataSource class that provides the interface to use in your concrete classes

from abc import ABC, abstractmethod

class FrontEnd:
    def __init__(self, data_source):
        self.data_source = data_source
        
    def display_data(self):
        data = self.data_source.get_data()
        print("Display data: ", data)
        
class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass
    
class Database(DataSource):
    def get_data(self):
        return "Data from the database"
    
class API(DataSource):
    def get_data(self):
        return "Data from the API"

db_front_end = FrontEnd(Database())
db_front_end.display_data()

api_front_end = FrontEnd(API())
api_front_end.display_data()
