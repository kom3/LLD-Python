"""
The Singleton Design Pattern is a creational pattern that ensures a class has only one instance while providing a global point of access to it. In Python, this is commonly used for managing shared resources like database connections, logging systems, or configuration managers. 

Core Implementation Methods

1. The "Pythonic" Singleton (Using __new__)
Python's __new__ method is responsible for creating a new instance. By overriding it, you can control the instantiation to always return the same object. 
This approach involves checking if an instance already exists within the __new__ method and creating a new one only if it doesn't. You can find a code example in the referenced web document. 
"""

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            # Create the instance only if it doesn't exist
            cls._instance = super().__new__(cls)
        return cls._instance

# Usage
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True


"""
2. Thread-Safe Singleton
To handle multi-threaded environments where multiple threads might try to create an instance concurrently, a lock can be used to ensure only one thread can proceed with the creation logic at a time. A code example for a thread-safe singleton is available in the referenced web document.
"""

import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        # Double-checked locking to optimize performance
        if cls._instance is None:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance
    


"""
3. Metaclass Implementation
A metaclass can provide a more reusable way to implement the singleton pattern, separating the pattern's logic from the class's specific business logic. You can see an example of a metaclass implementation in the referenced web document. 
"""

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # Call the class's constructor only once
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    pass

# Both point to the same database connection object
db1 = DatabaseConnection()
db2 = DatabaseConnection()


"""
The "Borg" Pattern (Monostate)
Distinct from the standard Singleton, the Borg pattern allows for multiple instances of a class, but they all share the same state by referencing the same internal dictionary (__dict__). An example demonstrating the Borg pattern can be found in the referenced web document. 

Important Considerations for 2026
- Modules as Singletons: Python modules themselves function as singletons as they are imported only once. Some developers prefer using a module-level instance rather than creating a dedicated Singleton class.
- Anti-Pattern Debate: Singletons are often viewed critically because they introduce global state, which can complicate unit testing and debugging due to hidden dependencies.
- Use Cases: Singletons are best used in scenarios where a single, unified source is truly essential, such as managing hardware device interfaces or centralized configuration data. 
"""

class Borg:
    _shared_state = {}

    def __init__(self):
        # All instances share the same attributes
        self.__dict__ = self._shared_state

# Usage
b1 = Borg()
b2 = Borg()
b1.config = "Value A"
print(b2.config)  # Output: Value A
print(b1 is b2)   # Output: False (Distinct objects, shared state)