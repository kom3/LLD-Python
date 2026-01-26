"""
The Composite Design Pattern is a structural pattern used in Low-Level Design (LLD) to represent "part-whole" hierarchies. It allows you to compose objects into tree structures and treat individual objects (Leaves) and compositions of objects (Composites) uniformly. 

Core Components:
    - Component: An abstract base class or interface that defines common operations for both simple and complex objects.
    - Leaf: A basic building block with no children that implements the Component's behavior directly.
    - Composite: A container that holds children (both Leaves and other Composites). It delegates work to its children and often "sums up" the results.
    - Client: Interacts with all elements through the common Component interface, unaware of whether an object is a single leaf or a large composition.
"""



from abc import ABC, abstractmethod

# 1. Component Interface
class FileSystemItem(ABC):
    @abstractmethod
    def get_size(self) -> int:
        pass

# 2. Leaf Class
class File(FileSystemItem):
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def get_size(self) -> int:
        return self.size

# 3. Composite Class
class Folder(FileSystemItem):
    def __init__(self, name: str):
        self.name = name
        self.children = []

    def add(self, item: FileSystemItem):
        self.children.append(item)

    def get_size(self) -> int:
        # Recursively sums up sizes of all children
        return sum(child.get_size() for child in self.children)

# 4. Client Code
if __name__ == "__main__":
    file1 = File("Data.txt", 100)
    file2 = File("Pic.png", 500)
    
    sub_folder = Folder("Images")
    sub_folder.add(file2)
    
    root_folder = Folder("Root")
    root_folder.add(file1)
    root_folder.add(sub_folder)

    # Client treats File and Folder uniformly
    print(f"Total size: {root_folder.get_size()} KB") # Output: 600 KB



"""
When to Use
    - Tree Structures: When your model can be represented as a hierarchy, such as UI component trees, organizational charts, or file systems.
    - Uniformity: When you want to eliminate complex if-else or isinstance checks that distinguish between single items and groups.
    - Recursive Operations: When you need to perform calculations that aggregate data from an entire structure.

Pros:
    - Uniformity: Clients treat all elements identically.
    - Open/Closed Principle: Easy to add new component types without changing existing code.
    - Recursive Clarity: Simplifies management of deep nested structures.

Cons:
    - Complexity: Designing a common interface for leaves and composites can be difficult.
    - Type Safety: General interface may expose irrelevant methods to leaf nodes.
    - Overhead: Deep tree traversal can impact performance in complex systems.
"""