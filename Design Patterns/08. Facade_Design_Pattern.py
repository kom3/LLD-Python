"""
The Facade Design Pattern is a structural pattern that provides a simplified, high-level interface to a complex subsystem. While the Adapter pattern aims for interoperability (making incompatible things work together), the Facade pattern focuses on simplicity (hiding complexity behind a single entry point). 

Core Components
    - Facade Class: The entry point that orchestrates multiple subsystem classes.
    - Subsystem Classes: Specialized classes that perform low-level operations. They are unaware of the Facade.
    - Client: Interacts only with the Facade to perform complex tasks with one call. 
"""

# 1. Subsystem Classes (The complex parts)
class Lights:
    def dim(self, level): print(f"Lights dimmed to {level}%")

class Projector:
    def on(self): print("Projector turned on")
    def set_input(self, source): print(f"Projector input set to {source}")

class SoundSystem:
    def set_volume(self, level): print(f"Sound volume set to {level}")

# 2. Facade Class (The simplified interface)
class HomeTheaterFacade:
    def __init__(self):
        # Composition: Holding references to subsystems
        self.lights = Lights()
        self.projector = Projector()
        self.sound = SoundSystem()

    def watch_movie(self, movie_name):
        print(f"--- Preparing to watch {movie_name} ---")
        self.lights.dim(10)
        self.projector.on()
        self.projector.set_input("DVD")
        self.sound.set_volume(20)
        print("Movie started!")

# 3. Client Code
if __name__ == "__main__":
    # Client doesn't need to know how to set up the projector or lights
    theater = HomeTheaterFacade()
    theater.watch_movie("Inception")


"""
When to Use
    - Complex Subsystems: When a system has many moving parts and you want to offer a simple API.
    - Layering: When you want to define entry points for different layers of an application.
    - Decoupling: To minimize dependencies between client code and internal library changes.

Facade vs. Adapter
-------------------------------------------------------------------------------------------------------------------------|
Feature 	    |           Facade Pattern	                     |       Adapter Pattern                                 |
-------------------------------------------------------------------------------------------------------------------------|
Primary Intent	|   Provide a simpler interface.	             |  Make incompatible interfaces compatible.             |
Scope	        |   Usually wraps multiple subsystem classes.	 |  Typically wraps a single class.                      |
Timing	        |   Often used during design to simplify usage.  |	Used to integrate existing legacy or 3rd-party code. |
-------------------------------------------------------------------------------------------------------------------------|
"""