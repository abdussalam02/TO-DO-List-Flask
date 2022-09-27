"""
Inheritance
The proceess of inheriting the properties of parents class by child class is known as inheritance. The main purpose of inheritance
is reusability of code because we can use the existing class to create a new class.
Also, a child class can provide its specific implementation to the methods of the parent class.

Types of Inheritance 
1) Single: When a single child class inherits from single parent class it is known as single inheritance.
2) Multiple: When a child class inherits from multiple parent class is know as miltiple inheritance
3) Multilevel: When a child class inherits from another child class or a class derieved from parent class is known as multilevel
4) Hierarchical: When multiple child class inherits from a single parent class it is known as hierarchial inheritance
5) Hybrid: When all or most of the condition above is met it is called as hybrid inheritance
"""

class Mistech:
    def __init__(self, product, price):
        self.product = product
        self.price = price
        
    def display(self):
        print("This is our catalogue of product in our Mistech store")



class Intel(Mistech):
    def __init__(self, product, price, company, quantity):
        super().__init__(product, price)
        self.company = company
        self._quantity = quantity

    def display(self):
        print(self.company, self.product, "for Rs.", self.price)


class Ryzen(Intel, Mistech):
    def display(self):
        print(self.company, self.product, "for Rs.", self.price)

    def set_name(self):
        return self._quantity


mis = Mistech("Processor", 12200)
mis.display()

ent = Intel("Processor", 12200, "Intel", 55)
ent.display()

ryz = Ryzen("Processor", 10000, "Ryzen", 85)
ryz.display()

ryz.set_name()