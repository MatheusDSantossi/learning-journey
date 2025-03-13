from facade_method import *

class OrderFacade:
    def __init__(self):
        self.inventory = Inventory()
        self.payment = Payment()
        self.notification = Notification()
        
    def place_order(self, product_id, quantity, amount):
        if self.inventory.check_stock(product_id):
            if self.payment.process_payment(amount):
                self.inventory.update_stock(product_id, -quantity)
                self.notification.send_confirmation(product_id)
                print("Order placed successfully")
            else:
                print("Payment processing failed")
                
        else:
            print("Product is out of stock")
            
if __name__ == "__main__":
    facade = OrderFacade()
    facade.place_order(product_id=21, quantity=20, amount=2000)


