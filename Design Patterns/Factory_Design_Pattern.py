"""
The Factory Design Pattern is a creational pattern used in Python to delegate the responsibility of object creation to a separate class or method. Instead of calling a class constructor directly (e.g., car = Toyota()), you ask a "factory" to provide the object you need (e.g., car = Factory.get_car("toyota")). 

This pattern is especially useful when your code needs to create various types of similar objects but should remain decoupled from their specific implementation details. 


Key Components
    - Product Interface: A common interface (usually an abstract base class in Python using abc.ABC) that defines the methods all concrete products must have.
    - Concrete Products: The actual classes (like Car or Bike) that implement the Product interface.
    - Creator (Factory): The component that contains the "factory method" to return new product instances based on input.
"""



"""
Why Use It?
- Loose Coupling: The client code doesn't need to know the specific class names of the objects it uses, only the interface.

- Scalability: You can add new product types (e.g., a Bird class) by updating only the factory, rather than searching through your entire codebase for every place an object is created.

- Centralized Logic: All complex object creation logic (like setting default parameters or handling environment-specific configurations) is contained in one place.

- Open-Closed Principle: The system is open for extension (adding new products) but closed for modification (existing client code remains untouched). 



Real-World Scenarios:
- Database Connections: A factory can return a MySQL, PostgreSQL, or SQLite connection based on a configuration file.

- File Parsers: Creating different parsers (JSON, XML, CSV) depending on a file's extension.

- Payment Gateways: Switching between Stripe, PayPal, or Square depending on user selection at runtime. 
"""



"""
In software design, the "Factory" pattern is typically categorized into three main types based on their level of abstraction and complexity. 

1. Simple Factory
- This is the most basic version and is often considered a programming idiom/principle rather than a formal design pattern. 
- Structure: A single class with a static method that uses conditional logic (e.g., if/else or match/case) to create and return different objects based on input.
- Best For: Small projects where you only have one layer of related objects and the creation logic is straightforward.
- Analogy: A vending machine with buttons for specific products; you press a button, and it gives you exactly that item.
"""

from abc import ABC, abstractmethod

# 1. Product Interface
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# 2. Concrete Products
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# 3. Factory Class
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type): # A static method does not receive an implicit first argument (self).
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Client Code
factory = AnimalFactory()
pet = factory.create_animal("dog")
print(pet.speak())  # Output: Woof!



"""
2. Factory Method
- A formal creational pattern that uses inheritance to delegate object creation to subclasses. 
- Structure: An abstract base class defines a "factory method," but subclasses override it to specify which concrete class to instantiate.
- Best For: When you want to adhere to the Open/Closed Principle—you can add new product types by creating new subclasses without modifying existing code.
- Analogy: A restaurant with different specialized chefs (subclasses); each chef knows how to prepare their own specific signature dish. 
"""

from abc import ABC, abstractmethod

# Base Creator
class TransportManager(ABC):
    @abstractmethod
    def create_transport(self): pass

    def plan_delivery(self):
        transport = self.create_transport()
        return f"Delivering via {transport.deliver()}"

# Concrete Creators
class TruckManager(TransportManager):
    def create_transport(self): return Truck()

class ShipManager(TransportManager):
    def create_transport(self): return Ship()

# Concrete Products
class Truck:
    def deliver(self): return "Land"

class Ship:
    def deliver(self): return "Sea"

# Usage
manager = TruckManager()
print(manager.plan_delivery()) # Output: Delivering via Land


"""
3. Abstract Factory
- This is the highest level of abstraction, often called a "factory of factories". 
- Structure: Provides an interface for creating families of related or dependent objects without specifying their concrete classes. Instead of creating just one object, it returns an object containing multiple factory methods for an entire suite of products.
- Best For: Cross-platform applications (e.g., a UI toolkit that must create buttons, checkboxes, and menus that all look consistent for either Windows or macOS).
- Analogy: A department store with different departments (concrete factories); each department sells a full family of related products (e.g., the electronics department vs. the clothing department). 

"""

class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self): pass
    @abstractmethod
    def create_table(self): pass

# Family 1: Modern
class ModernFactory(FurnitureFactory):
    def create_chair(self): return ModernChair()
    def create_table(self): return ModernTable()

# Family 2: Vintage
class VintageFactory(FurnitureFactory):
    def create_chair(self): return VintageChair()
    def create_table(self): return VintageTable()

# Concrete Products (ModernChair, VintageChair, etc. would be defined here)
# The base interface for all Chairs
class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass

# The base interface for all Tables
class Table(ABC):
    @abstractmethod
    def place_item(self):
        pass

# --- Modern Variants ---
class ModernChair(Chair):
    def sit_on(self):
        return "Sitting on a sleek modern chair."

class ModernTable(Table):
    def place_item(self):
        return "Placing a laptop on a glass modern table."

# --- Vintage Variants ---
class VintageChair(Chair):
    def sit_on(self):
        return "Sitting on a carved wooden vintage chair."

class VintageTable(Table):
    def place_item(self):
        return "Placing a tea set on a heavy oak vintage table."


# Usage
def setup_room(factory: FurnitureFactory):
    chair = factory.create_chair()
    table = factory.create_table()
    # Now you have a matching set!

setup_room(ModernFactory())