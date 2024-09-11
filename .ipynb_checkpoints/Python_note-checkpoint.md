## dufault global variables and built-ins

Special Variables
__name__: Indicates the name of the current module. It is set to "__main__" when the script is run directly.
__file__: Contains the path to the script being executed (not always available, depending on the execution context).
__doc__: Contains the docstring of the module, if present.
__package__: Indicates the package name of the module.
__loader__: Contains the loader used to load the module.
__spec__: Contains the module spec (module specification).

Built-in Constants
None: Represents the absence of a value.
True: Boolean true value.
False: Boolean false value.
Ellipsis: The ... object, used in slicing and other contexts.
NotImplemented: Indicates that an operation is not implemented for a given type.

Built-in Functions
Python provides a wide range of built-in functions that are always available. Here are some commonly used built-in functions:

Type Conversion Functions:

int(), float(), str(), list(), tuple(), dict(), set(), bool(), complex(), bytes(), bytearray()
Mathematical Functions:

abs(), min(), max(), sum(), round(), pow(), divmod()

Iterables and Iteration:

len(), range(), enumerate(), map(), filter(), zip(), sorted(), reversed(), all(), any(), next(), iter()
String Handling:

chr(), ord(), format(), ascii(), repr()
Object and Class Handling:

type(), isinstance(), issubclass(), hasattr(), getattr(), setattr(), delattr(), vars(), dir(), id(), callable()
Input/Output:

print(), input(), open()
Utility Functions:

help(), eval(), exec(), compile(), globals(), locals(), memoryview(), object(), property(), staticmethod(), classmethod(), super()
Example
You can see the list of all built-in functions and constants by inspecting the builtins module:

import builtins

print(dir(builtins))
This will print a list of all the built-in functions, constants, and exceptions available in Python.

# Class
class MyClass:
    def __call__(self): # MyClass() will call the method
        pass

class MyClass:
    def __repr__(self):   # implement repr method for the class
        return "MyClass()"

#  __init__(self)
The __init__ method is called immediately after an instance of the class is created. This happens when you call the class as if it were a function, which is known as instantiating the class.

Function Objects, Decorators, Custom Callables
# __call__(self):
The __call__ method is called when you use parentheses () to call an instance of a class. This allows you to use the instance as if it were a regular function.

# def __str__(self):
    return "This is a MyClass object"
    
When you pass an object to the print() function, it implicitly calls the str() function on the object, which in turn calls the __str__ method
for list and dict object, will call internal __str__ when call print(the object) or str(the object)


# Decorators
Decorators are functions that modify the behavior of other functions or methods.