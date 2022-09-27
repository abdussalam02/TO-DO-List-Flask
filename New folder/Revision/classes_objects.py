# Classes and Objects
"""
Class: The class is a user-defined data structure that binds the data members and methods into a single unit. 

Objects: An object is an instance of a class. It is a collection of attributes (variables) and methods.
         We use the object of a class to perform actions.

Attributes(states) are of two types: 
1) Instance variable: It is initialized inside construct or any methods
2) Class variable: It is initialized inside class but out of any method scope

Methods(behaviours) are of three types
1) Instance method: It accesses and modifies Instance variable and it varies object to object
2) Class Method: It accesses and modifies class variable and it is same for every objects
3) Static Method: It can't access any class attributes. It performs its task in isolation.

"""
# This is a class initialization
class Aladdin(object): # class Aladdin: simplified way but works same
    
    x = 1 # This is a class variable
    
    # This is a constructor
    def __init__(self, age):
        self.name = "Aladdin" # This is instance variable with default value
        self.age = age # This is also an instance variable using parameter
    
    # This is an instance method with no parameters
    def nothing(self):
        weight = 56
        print("Aladdin's weight:", weight)
        
    # This is an instance method with parameter
    def show(self, height):
        print("Aladdin's Detail: ", self.name, self.age, height, sep=",")
        
        
    # This is a static method
    def display(self):
        pass
    
    # This is a class method
    @classmethod
    def value_update(cls, y):
        cls.x = y
        
assign = Aladdin(19) # Insatiation of object to a class() with a parameter for construct

print(assign.name) # calling instance attribute

assign.display() # calling a method

assign.show(5.5) # calling a method with parameters

del assign.name # deleting object properties

del emp # deleting object