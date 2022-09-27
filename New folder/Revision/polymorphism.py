"""
Polymorphism
Polymorphism is the ability of an object to perform the same action in many different ways.
In polymorphism, a method can process objects differently depending upon the class type or data type. len() is a fine example of polymorphism
It is mainly used with inheritance and we can override builtin functions too

Method Overloading: The process of calling the same method with different parameters is known as method overloading.
                    Python does not support method overloading. Python considers the last defined method even if you overload the method.
Method Overriding: When method name of parent and child class are same but they perform different functionality is known as method overloading.
"""

class Vehicle:
    x = 0
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print('Details:', self.name, self.color, self.price)

    def max_speed(a):
        print('Vehicle max speed is 150')

    def change_gear(self):
        print('Vehicle change 6 gear')


# inherit from vehicle class
class Car(Vehicle):
    
    def __init__(self, name, color, price, make):
        super().__init__(name, color, price)
        self.make = make    
    
    def max_speed(self):
        print('Car max speed is 240')

    def change_gear(self):
        print('Car change 7 gear')


# Car Object
car = Car('Car x1', 'Red', 20000, 'audi')
car.show()
# calls methods from Car class
car.max_speed()
car.change_gear()

# Vehicle Object
vehicle = Vehicle('Truck x1', 'white', 75000)
vehicle.show()
# calls method from a Vehicle class
vehicle.max_speed()
vehicle.change_gear()