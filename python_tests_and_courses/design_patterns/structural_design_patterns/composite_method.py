"""Here we attempt to make an organizational hierarchy with sub-organization,
 which may have subsequent sub-organizations, such as:
GeneralManager                                   [Composite]
      Manager1                                   [Composite]
              Developer11                        [Leaf]
              Developer12                        [Leaf]
      Manager2                                   [Composite]
              Developer21                        [Leaf]
              Developer22                        [Leaf]"""

class LeafElement:
    """Class representing objects at the bottom or Leaf of the hierarchy tree."""
    
    def __init__(self, *args):
        """Takes the first positional argument and assisgns to member variable position"""
        self.position = args[0]
        
    def showDetails(self):
        """Displays the details of this child element"""
        # return f"Leaf element: {self.position}"
        print("\t", end="")
        print(self.position)
        
class CompositeElement:
    """Class representing objects at any level of the hierarchy tree except for the bottom or leaf level. Maintains the child objects by adding and removing them from the tree structure.""" 
    def __init__(self, *args):
        """Takes the first positional argument and assigns to member variable position. Initializes a list of children elemnts"""
        self.position = args[0]
        self.children = []
    
    def add(self, child):
        """Adds the supplied child element to the list of children"""
        self.children.append(child)
    
    def remove(self, child):
        """Removes the supplied child element from the list of children"""
        self.children.remove(child)
    
    def showDetails(self):
        """Displays the details of the component element first then, iterates over each of its children, prints their details by calling their showDeatils() method"""
        print(self.position)
        for child in self.children:
            print("\t", end="")
            child.showDetails()
            
# Main method
if __name__ == "__main__":
    topLevelMenu = CompositeElement("GeneralManager")
    subMenuItem1 = CompositeElement("Manager1")
    subMenuItem2 = CompositeElement("Manager2")
    subMenuItem11 = LeafElement("Developer11")
    subMenuItem12 = LeafElement("Developer12")
    subMenuItem21 = LeafElement("Developer21")
    subMenuItem22 = LeafElement("Developer22")
    subMenuItem1.add(subMenuItem11)
    subMenuItem1.add(subMenuItem12)
    subMenuItem2.add(subMenuItem22)
    subMenuItem2.add(subMenuItem22)

    topLevelMenu.add(subMenuItem1)
    topLevelMenu.add(subMenuItem2)
    topLevelMenu.showDetails()

# Applicability
# Requirement of Nested Tree Structure: It is highly preferred to use Composite Method when you are need of producing the nested structure of tree which again include the leaves objects and other object containers.
# Graphics Editor: We can define a shape into types either it is simple for ex – a straight line or complex for ex – a rectangle. Since all the shapes have many common operations, such as rendering the shape to screen so composite pattern can be used to enable the program to deal with all shapes uniformly.
