"""
The Proxy Design Pattern is a structural pattern that provides a surrogate or placeholder for another object to control access to it. In Low-Level Design (LLD), a proxy acts as an intermediary that can add functionality like lazy initialization, access control, logging, or caching without modifying the original "Real Subject" or the client code. 

Core Components
 - Subject (Interface): An abstract class or interface defining common operations for both the real object and the proxy.
 - Real Subject: The actual object that performs the core business logic or resource-heavy tasks.
 - Proxy: Holds a reference to the Real Subject and implements the same interface to intercept and manage client requests. 

Types of Proxies
    - Virtual Proxy: Delays the creation of expensive-to-instantiate objects until they are actually needed (Lazy Loading).
    - Protection Proxy: Controls access to the real object based on permissions or authentication.
    - Caching Proxy: Stores results of expensive operations to avoid redundant work for repeated requests.
    - Remote Proxy: Acts as a local representative for an object located in a different address space or server. 
"""


# -------------------------------------------------------
# Python Implementation (Virtual Proxy)
# -------------------------------------------------------

"""
This example uses a virtual proxy to defer the heavy loading of a database connection until a query is actually executed.
"""

from abc import ABC, abstractmethod

# 1. Subject Interface
class Database(ABC):
    @abstractmethod
    def execute_query(self, query: str):
        pass

# 2. Real Subject: Heavy to initialize
class RealDatabase(Database):
    def __init__(self):
        print("Connecting to heavy Database... (Takes time/resources)")
    
    def execute_query(self, query: str):
        print(f"Executing query: {query}")

# 3. Proxy: Implements the same interface
class DatabaseProxy(Database):
    def __init__(self):
        self._real_db = None  # Reference to the real object

    def execute_query(self, query: str):
        # Lazy Initialization: Create real object only when needed
        if self._real_db is None:
            self._real_db = RealDatabase()
        
        # Additional logic (e.g., logging) can be added here
        print(f"Proxy: Logging request for '{query}'")
        self._real_db.execute_query(query)

# Client Code
def run_app(db: Database):
    print("Client: Application started, but no DB connection yet.")
    # Connection only happens here, when actually needed
    db.execute_query("SELECT * FROM users")

proxy = DatabaseProxy()
run_app(proxy)





# -------------------------------------------------------
# Protection Proxy (Access Control)
# -------------------------------------------------------
"""
A protection proxy controls access to the original object based on access rights or permissions. 
"""


class SensitiveData:
    """The Real Subject"""
    def read(self):
        return "Top secret information."

class ProtectionProxy:
    """The Proxy: Checks for authorization before allowing access"""
    def __init__(self, real_subject, user_role):
        self._real_subject = real_subject
        self._user_role = user_role

    def read(self):
        if self._user_role == "ADMIN":
            return self._real_subject.read()
        return "Access Denied: You do not have permissions."

# Usage
real_data = SensitiveData()
admin_proxy = ProtectionProxy(real_data, "ADMIN")
guest_proxy = ProtectionProxy(real_data, "GUEST")

print(admin_proxy.read())  # Output: Top secret information.
print(guest_proxy.read())  # Output: Access Denied: You do not have permissions.



# -------------------------------------------------------
# Caching Proxy (Performance Optimization)
# -------------------------------------------------------
"""
A caching proxy stores the results of expensive operations to avoid redundant work when the same request is made again.
"""

import time

class HeavyCalculator:
    """The Real Subject: Performs an expensive computation"""
    def compute(self, x):
        print(f"Thinking hard about {x}...")
        time.sleep(2)  # Simulating a heavy task
        return x * x

class CachingProxy:
    """The Proxy: Stores results to avoid repeated heavy tasks"""
    def __init__(self, real_subject):
        self._real_subject = real_subject
        self._cache = {}

    def compute(self, x):
        if x not in self._cache:
            self._cache[x] = self._real_subject.compute(x)
        else:
            print(f"Retrieving cached result for {x}")
        return self._cache[x]

# Usage
calc = HeavyCalculator()
proxy = CachingProxy(calc)

print(proxy.compute(10))  # First call: Performs actual computation
print(proxy.compute(10))  # Second call: Returns cached result instantly



# -------------------------------------------------------
# Remote Proxy (Inter-Process Communication)
# -------------------------------------------------------

"""
A remote proxy acts as a local representative for an object that exists in a different address space, such as a remote server. In Python, this is often implemented using frameworks like gRPC or RPyC.
"""

# Concept: Remote Proxy (Stub)
class RemoteServiceProxy:
    """The Proxy: Hides the complexity of network calls"""
    def __init__(self, host, port):
        self.address = (host, port)
        # In a real scenario, this would initialize a network socket/connection

    def get_user_data(self, user_id):
        print(f"Proxy: Packaging request for user {user_id} over network...")
        # 1. Serialize request
        # 2. Send over socket to self.address
        # 3. Receive and deserialize response
        return {"id": user_id, "name": "Remote User", "status": "Fetched via Proxy"}

# Client Code
proxy = RemoteServiceProxy("192.168.1.100", 50051)
# The client calls it as if it were a local object
data = proxy.get_user_data(42)
print(data)






"""
Key Benefits and Use Cases
    - Performance Optimization: By using a Virtual Proxy, you save memory and CPU by avoiding the creation of heavy objects that might never be used.
    - Security Layer: A Protection Proxy can act as a gatekeeper, verifying user roles before allowing access to sensitive data.
    - Transparency: The client remains unaware that it is interacting with a proxy rather than the real object because they share the same interface.


Comparison of Proxy Types
-------------------------------------------------------------------------------------------------------------------------------
    Type 	                        Purpose	                            Key Logic
-------------------------------------------------------------------------------------------------------------------------------
    Virtual	                        Delay instantiation	                if self._real_obj is None: self._real_obj = RealObj()
    Protection	                    Access control	                    if user.has_role('ADMIN'): self._real_obj.call()
    Caching	                        Store results	                    if key in self._cache: return self._cache[key]
    Remote	                        Network abstraction	                network_send(request) -> receive(response)
-------------------------------------------------------------------------------------------------------------------------------
"""