"""
The Command Design Pattern is a behavioral pattern that turns a request into a standalone object. In Low-Level Design (LLD), it is used to decouple the object that invokes an operation (the Invoker) from the one that knows how to perform it (the Receiver). 

Core Components
 - Command Interface: Defines the contract, usually an execute() method.
 - Concrete Commands: Implement the interface and bind a Receiver to a specific action.
 - Receiver: The actual object that performs the work (e.g., a Light, a Bank Account).
 - Invoker: Triggers the command. It holds a reference to a command but does not know its internal logic.
 - Client: Creates the concrete command objects and sets their receivers. 
"""

from abc import ABC, abstractmethod

# 1. Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# 2. Receiver (The object doing the work)
class Light:
    def on(self):
        print("Light is ON")

    def off(self):
        print("Light is OFF")

# 3. Concrete Commands
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()

# 4. Invoker (e.g., a Remote Control)
class RemoteControl:
    def __init__(self):
        self.history = []

    def press_button(self, command: Command):
        command.execute()
        self.history.append(command)

    def press_undo(self):
        if self.history:
            command = self.history.pop()
            command.undo()

# Client Code
if __name__ == "__main__":
    living_room_light = Light()
    light_on = LightOnCommand(living_room_light)
    
    remote = RemoteControl()
    remote.press_button(light_on)  # Output: Light is ON
    remote.press_undo()            # Output: Light is OFF



"""
Key Advantages in LLD
    - Single Responsibility Principle: You can separate classes that invoke operations from classes that perform them.
    - Open/Closed Principle: You can introduce new commands without breaking existing client code.
    - Macro Support: You can combine multiple commands into a single "macro" command object to execute them in sequence.
    - Transactional Behavior: Commands can be queued or logged, allowing for rollbacks if a sequence of operations fails. 


Common Use Cases
    - GUI Buttons: Each button is assigned a command object that executes when clicked.
    - Task Queuing: Wrapping jobs in command objects to be processed later by worker threads.
    - Game Development: Encapsulating player inputs as commands to allow for replaying or undoing moves.
"""