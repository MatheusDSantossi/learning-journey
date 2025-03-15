from abc import ABC, abstractmethod

class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)
        
    def total_price(self):
        total = 0
        for i in range(len(self.items)):
            total += self.quantities[i] * self.prices[i]
            
        return total
    
    # def pay(self, payment_type, security_code):
    #     if payment_type == "credit":
    #         print("Processing credit payment type...")
    #         print(f"Verifying security code {self.security_code}")
    #         self.status = "paid"
    #     elif payment_type == "debit":
    #         print("Processing debit payment type...")
    #         print(f"Verifying security code {security_code}")
    #         self.status = "paid"
    #     else:
    #         raise Exception(f"Unkown Payment type: {payment_type}")
        
    def setStatus(self, status):
        self.status = status
        
    def getStatus(self):
        return self.status

class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass

class SMSAuth(Authorizer):
    authorized = False
    
    def verify_code(self, code):
        print(f"Verifying code {code}")
        self.authorized = True
        
    def is_authorized(self):
        return self.authorized

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass

class NotARobot(Authorizer):
    authorized = False
    
    def not_a_robot(self):
        print("Are you a robot?")
        self.authorized = True
        
    def is_authorized(self):
        return self.authorized

    
# class PaymentProcessor_SMS(PaymentProcessor):
#     verified = False
    
#     @abstractmethod
#     def auth_sms(self, code):
#         pass
    
#     def setVerified(self, verified):
#         self.verified = verified
        
#     def getVerified(self):
#         return self.verified
    
class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code
    
    # def auth_sms(self, code):
    #     raise Exception("Credit card payments don't support SMS code authorization.")    
    
    def pay(self, order):
        print("Processing credit payment type...")
        print(f"Verifying security code {self.security_code}")
        order.setStatus("paid") 
        
class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer: Authorizer):
        self.authorizer = authorizer
        self.security_code = security_code
        
    # def auth_sms(self, code):
    #     raise Exception("Credit card payments don't support SMS code authorization.")    
        
    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("SMS code not verified.")
        print("Processing debit payment type...")
        print(f"Verifying security code {self.security_code}")
        order.setStatus("paid") 
        
class BitcoinPaymentProcessor(PaymentProcessor):
    def __init__(self, wallet_address, authorizer: Authorizer):
        self.authorizer = authorizer
        self.wallet_address = wallet_address
        
    # def auth_sms(self, code):
    #     print(f"Verifying SMS code {code}")
    #     self.verified = True
        
    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("SMS code not verified.")
        
        print("Processing BTC payment type...")
        print(f"Verifying wallet address {self.wallet_address}")
        order.setStatus("paid") 
        
order = Order()

order.add_item("Apple", 10, 900.50)
order.add_item("SSD", 1, 200.50)
order.add_item("USB Cable", 1, 2)
# print(order.getStatus())

print(order.total_price())

authorizer = NotARobot()
processor = BitcoinPaymentProcessor("$asdasdas0123eaw#20", authorizer)
authorizer.not_a_robot()
processor.pay(order)
# print(order.getStatus())