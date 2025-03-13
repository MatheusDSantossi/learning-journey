# The facade method is one good example to use in an e-commerce where customers can place orders, make payments, and receive notifications.

class Inventory:
    def check_stock(self, product_id):
        print(f"Checking stock for product {product_id}")
        # Simualte stock check
        return True
    
    def update_stock(self, product_id, quantity):
        print(f"Updating stock for product {product_id} by {quantity}")
        
class Payment:
    def process_payment(self, amount):
        print(f"processing payment of ${amount}")
        # simulate payment processing
        return True
    
class Notification:
    def send_confirmation(self, order_id):
        print(f"Sending confirmation for order {order_id}")
