"""A separate class for Item"""
class Item:
    # constructor function with price and discount
    def __init__(self, price, discount_strategy=None):
        # Take price and discount strategy
        self.price = price
        self.discount_strategy = discount_strategy
        
    # A separate function for price after discount
    def price_after_discount(self):
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0
        return self.price - discount
    
    def __repr__(self):
        statement = "Price: {}, price after discount: {}"
        return statement.format(self.price, self.price_after_discount())
    
"""function dedicated to On Sale Discount"""
def on_sale_discount(order):
    return order.price * 0.25 + 20

"""function dedicated to 20% Discount"""
def twenty_percent_discount(order):
    return order.price * 0.20

# Main function
if __name__ == '__main__':
    print(Item(20000))
    
    # With discount strategy as 20 % discount
    print(Item(20000, discount_strategy=twenty_percent_discount))
    
    # With discount strategy as On Sale discount
    print(Item(20000, discount_strategy=on_sale_discount))

"""
Advantages

Open/Closed principle: Its always easy to introduce the new strategies without changing the client’s code.
Isolation: We can isolate the specific implementation details of the algorithms from the client’s code.
Encapsulation: Data structures used for implementing the algorithm are completely encapsulated in Strategy classes. Therefore, the implementation of an algorithm can be changed without affecting the Context class
Run-time Switching: It is possible that application can switch the strategies at the run-time.

Disadvantages

Creating Extra Objects: In most cases, the application configures the Context with the required Strategy object. Therefore, the application needs to create and maintain two objects in place of one.
Awareness among clients: Difference between the strategies should be clear among the clients to able to select a best one for them.
Increases the complexity: when we have only a few number of algorithms to implement, then its waste of resources to implement the Strategy method.

Applicability 

Lot of Similar Classes: This method is highly preferred when we have a lot of similar classes that differs in the way they execute.
Conquering Isolation: It is generally used to isolate the business logic of the class from the algorithmic implementation.
"""
