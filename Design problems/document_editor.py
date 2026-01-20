"""
Required components/elements.
We can use either top-down or bottom-up approach:
Here we are using Bottom-Up approach: listing components from low level to high level.

1. DocumentElements: Text, Image, Newline, Tab...etc

2. Document
    - Comprises functionalities like storage and render

3. PersistenceStorage
    - DB storage
    - File storage

4. Document Editor
    - Should be able to process the client interactions by allowing to perform the functionalities like add_elements, render and save
"""

from abc import ABC, abstractmethod


class DocumentElement(ABC):
    @abstractmethod
    def render(self):
        pass

class TextElement(DocumentElement):
    def __init__(self, text):
        self.text = text
    
    def render(self):
        return self.text
    
class ImageElement(DocumentElement):
    def __init__(self, img):
        self.img = img
    
    def render(self):
        return f"<img src='{self.img}' ></img>"


class NewLineElement(DocumentElement):
    def __init__(self):
        self.newline = "\n"
    
    def render(self):
        return self.newline
    
class TabElement(DocumentElement):
    def __init__(self):
        self.tab = "\t"
    
    def render(self):
        return self.tab



#@@@@@@@@@@@@@@@@


class Document():
    def __init__(self):
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def render(self):
        result = ""
        for element in self.elements:
            result += element.render()
        return result


#@@@@@@@@@@@@@@@@


class PersistenceStorage(ABC):
    @abstractmethod
    def save(self, data):
        pass


class FileStorage(PersistenceStorage):
    def save(self, data):
        with open("output_doc.txt", "w") as f:
            f.write(data)
        print("Document saved to output_doc.txt")


class DBStorage(PersistenceStorage):
    def save(self, data):
        # DB save logic goes here
        print("Document saved to the database")


#@@@@@@@@@@@@@@@@


class DocumentEditor():
    def __init__(self, doc_obj, storage_obj):
        self.doc_obj = doc_obj
        self.storage_obj = storage_obj

    def add_text(self, text):
        self.doc_obj.add_element(TextElement(text))
    
    def add_image(self, img):
        self.doc_obj.add_element(ImageElement(img))

    def add_newline(self):
        self.doc_obj.add_element(NewLineElement())

    def add_tab(self):
        self.doc_obj.add_element(TabElement())

    def render_document(self):
        return self.doc_obj.render()
    
    def save(self):
        self.storage_obj.save(self.render_document())




#@@@@@@@@@@@@@@@@
# Client usage example:

document_obj = Document()
storage_obj = FileStorage()

document_editor_obj = DocumentEditor(document_obj, storage_obj)

document_editor_obj.add_text("Hello, welcome to LLD using python")
document_editor_obj.add_newline()
document_editor_obj.add_image("py_img.jpg")
document_editor_obj.add_newline()
document_editor_obj.add_text("Excited to learn more about LLD principles and patterns.")
document_editor_obj.add_tab()
document_editor_obj.add_text("Let's Begin...")

print(document_editor_obj.render_document())

document_editor_obj.save() # currently uses file storage


# Interview Tips:

# In real time situation it's not possible to follow 100% SOLID principles all the time, there will be definitely some tradeoffs with every design, it's just that interviewer and the candidate should agree that those tradeoffs are acceptable.

# Sometimes a class might have knowledge of many neighboring classes and objects and that's fine until it follows the principle of least knowledge. Just because it has knowledge of multiple classes does not mean that it's breaking a single responsibility principle.



