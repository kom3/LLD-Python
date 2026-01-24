# 1. Requirements gathering
# 2. Identify core entities like classes and objects
# 3. Draw a UML Class diagrams and establish the relations
# 4. Align with the interviewer about the flow
# 5. Zoom in to 1-2 core components(writing pseudo code/working code depends on the interviewer ask)

"""
To design a system like Zomato in an hour for a Low-Level Design (LLD) interview, focus on the Order Placement and Tracking flow. This allows you to demonstrate the most critical design patterns and SOLID principles.

Core Design Patterns Used
    -Strategy Pattern: For flexible payment methods (UPI, Card, Cash).
    -Observer Pattern: To notify the User and Restaurant when the Order status changes.
    -Singleton Pattern: For central managers like RestaurantManager and OrderManager.
    -Factory Pattern: To create different types of Orders (Standard vs. Priority).
"""

from abc import ABC, abstractmethod
from typing import List
from enum import Enum

# --- 1. Enums and Entities ---
class OrderStatus(Enum):
    PENDING = "Pending"
    ACCEPTED = "Accepted"
    PREPARING = "Preparing"
    OUT_FOR_DELIVERY = "Out for Delivery"
    DELIVERED = "Delivered"

class MenuItem:
    def __init__(self, item_id: str, name: str, price: float):
        self.item_id = item_id
        self.name = name
        self.price = price

# --- 2. Strategy Pattern (Payment) ---
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class UPIPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paid ${amount} using UPI.")

class CardPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paid ${amount} using Credit/Debit Card.")

# --- 3. Observer Pattern (Order Tracking) ---
class OrderObserver(ABC):
    @abstractmethod
    def update(self, order_id: str, status: OrderStatus):
        pass

class User(OrderObserver):
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name

    def update(self, order_id: str, status: OrderStatus):
        print(f"Notification to User {self.name}: Order {order_id} is now {status.value}")

# --- 4. Main Order Class (Subject) ---
class Order:
    def __init__(self, order_id: str, user: User, items: List[MenuItem]):
        self.order_id = order_id
        self.user = user
        self.items = items
        self.status = OrderStatus.PENDING
        self.total_amount = sum(item.price for item in items)
        self._observers = [user]  # User is a default observer

    def set_status(self, status: OrderStatus):
        self.status = status
        self.notify_observers()

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self.order_id, self.status)

# --- 5. Singleton Managers ---
class OrderManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.orders = {}
        return cls._instance

    def place_order(self, user: User, items: List[MenuItem], payment: PaymentStrategy):
        order_id = f"ORD{len(self.orders) + 1}"
        payment.pay(sum(item.price for item in items))
        
        new_order = Order(order_id, user, items)
        self.orders[order_id] = new_order
        print(f"Order {order_id} placed successfully.")
        return new_order

# --- Client Usage (Revision Example) ---
if __name__ == "__main__":
    # 1. Setup Data
    user1 = User("U001", "Alice")
    pizza = MenuItem("M01", "Margherita Pizza", 12.0)
    coke = MenuItem("M02", "Coke", 2.0)

    # 2. Use Singleton Manager to Place Order
    manager = OrderManager()
    
    # 3. Strategy Pattern in action (choose payment method)
    my_order = manager.place_order(user1, [pizza, coke], UPIPayment())

    # 4. Observer Pattern in action (status updates)
    my_order.set_status(OrderStatus.ACCEPTED)
    my_order.set_status(OrderStatus.OUT_FOR_DELIVERY)


"""
Key Principles Applied
 -Single Responsibility (SRP): OrderManager handles logistics, PaymentStrategy handles money, and User handles notification display.
 -Open/Closed (OCP): You can add a CryptoPayment strategy without changing the OrderManager.
 -Dependency Inversion: OrderManager depends on the PaymentStrategy interface, not concrete classes like UPIPayment.
"""