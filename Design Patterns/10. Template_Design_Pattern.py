"""
The Template Design Pattern is a behavioral pattern that defines the skeleton of an algorithm in a base class, allowing subclasses to override specific steps without changing the overall structure. 

In Low-Level Design (LLD), it is widely used to enforce a consistent workflow across multiple implementations, following the "Hollywood Principle": "Don't call us, we'll call you".

Core Components
    - Abstract Class: Defines the Template Method (the fixed algorithm) and declares abstract methods for the steps that vary.
    - Concrete Class: Implements the abstract steps to provide specific behavior while inheriting the overarching workflow.
    - Hooks: Optional methods in the base class with empty or default behavior that subclasses can choose to override for additional flexibility. 

Implementation in Python

This example demonstrates a data processing pipeline where the sequence (Load → Process → Save) is fixed, but the logic for different file types varies.
"""

from abc import ABC, abstractmethod

# 1. Abstract Base Class (The Template)
class DataProcessor(ABC):
    def run_pipeline(self):
        """The Template Method: Defines the fixed sequence of steps."""
        self.load_data()
        self.process_data()
        self.hook_extra_validation()  # Optional hook
        self.save_results()

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def process_data(self):
        pass

    @abstractmethod
    def save_results(self):
        pass

    def hook_extra_validation(self):
        """Default hook: Subclasses can override this if needed."""
        pass

# 2. Concrete Implementation for CSV
class CSVDataProcessor(DataProcessor):
    def load_data(self):
        print("Loading data from CSV file...")

    def process_data(self):
        print("Cleaning and parsing CSV rows...")

    def save_results(self):
        print("Saving results to a local Database.")

# 3. Concrete Implementation for JSON
class JSONDataProcessor(DataProcessor):
    def load_data(self):
        print("Loading data from JSON API...")

    def process_data(self):
        print("Flattening nested JSON structures...")

    def save_results(self):
        print("Uploading results to Cloud Storage.")

    def hook_extra_validation(self):
        print("Running JSON schema validation...")

# Client Code
def execute_processor(processor: DataProcessor):
    processor.run_pipeline()

csv_proc = CSVDataProcessor()
execute_processor(csv_proc)


"""
When to Use
    - Enforce Consistency: When you have multiple classes with nearly identical algorithms that must follow a strict order.
    - Code Reuse: To pull up common code into a superclass and avoid duplication (DRY principle).
    - Framework Development: To provide a skeleton that users can extend by providing their own implementation for certain "plugs". 

Comparison: Template vs. Strategy
---------------------------------------------------------------------------------------
Feature 	        Template Method	                            Strategy Pattern
---------------------------------------------------------------------------------------
Mechanism	        Based on Inheritance	                    Based on Composition
Granularity	        Varies specific steps of an algorithm	    Varies the entire algorithm
Binding	            Static (fixed at compile time)	            Dynamic (can switch at runtime)
---------------------------------------------------------------------------------------
"""