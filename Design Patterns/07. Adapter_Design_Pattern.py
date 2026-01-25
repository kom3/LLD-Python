"""
The Adapter Design Pattern is a structural pattern in Low-Level Design (LLD) that allows incompatible interfaces to work together. It acts as a bridge or "wrapper" that translates the interface of an existing class into an interface that a client expects. 

Core Components
    - Target Interface: The interface your client code expects and uses.
    - Adaptee: The existing, incompatible class that contains the functionality you need but has a different interface.
    - Adapter: The bridge class that implements the Target interface and wraps an instance of the Adaptee to translate calls.
    - Client: The code that interacts with the Target interface, unaware that it is talking to an adapter. 
"""

from abc import ABC, abstractmethod

# 1. Target Interface: What the application expects
class USPlug(ABC):
    @abstractmethod
    def connect(self):
        pass

# 2. Adaptee: The incompatible legacy/third-party class
class EuropeanPlug:
    def specific_connect(self):
        return "Connected using European 2-pin socket."

# 3. Adapter: Bridges the gap
class PlugAdapter(USPlug):
    def __init__(self, european_plug: EuropeanPlug):
        self.adaptee = european_plug

    def connect(self):
        # Translates the call to the adaptee's interface
        return self.adaptee.specific_connect()

# 4. Client Code
def charge_laptop(plug: USPlug):
    print(plug.connect())

# Usage
euro_plug = EuropeanPlug()
adapter = PlugAdapter(euro_plug)
charge_laptop(adapter)  # Output: Connected using European 2-pin socket.


"""
When to Use
    - Integrating Legacy Code: When you want to use an old class with a new system without rewriting the old code.
    - Third-Party Libraries: When a third-party tool provides data or methods in a format that doesn't match your internal architecture.
    - Decoupling: To keep your client code independent of concrete third-party implementations. 

Key Benefits & Trade-offs
    - Pros: Follows the Single Responsibility Principle (separation of translation logic) and the Open/Closed Principle (add new adapters without changing existing code).
    - Cons: Adds complexity by introducing new classes and a slight runtime overhead due to the extra layer of indirection
"""