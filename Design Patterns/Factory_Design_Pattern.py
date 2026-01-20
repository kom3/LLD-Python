"""
The Factory Design Pattern is a creational pattern used in Python to delegate the responsibility of object creation to a separate class or method. Instead of calling a class constructor directly (e.g., car = Toyota()), you ask a "factory" to provide the object you need (e.g., car = Factory.get_car("toyota")). 

This pattern is especially useful when your code needs to create various types of similar objects but should remain decoupled from their specific implementation details. 


Key Components
    - Product Interface: A common interface (usually an abstract base class in Python using abc.ABC) that defines the methods all concrete products must have.
    - Concrete Products: The actual classes (like Car or Bike) that implement the Product interface.
    - Creator (Factory): The component that contains the "factory method" to return new product instances based on input.

    

Python Implementation Example

In this example, we use a factory to create different types of "Animal" objects without the client needing to know the specific classes.
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