from abc import ABC, abstractmethod

from order import Order
from authorizer import Authorizer, SMSAuth, NotARobot
from payment import CreditPaymentProcessor, DebitPaymentProcessor, PaypalPaymentProcessor



order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
# authorizer = SMSAuth()
authorizer = NotARobot()
processor = PaypalPaymentProcessor('mail@server', authorizer)
authorizer.not_a_robot()
processor.pay(order)
