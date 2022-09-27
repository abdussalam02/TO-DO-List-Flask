"""
Constructor is a special method used to create and initialize an object of a class

There are three types of constructor
1) Default Constructor: Python will provide default constructor, if no constructor is provided
2) Non Parameterized: The constructor wil not contain any parameters
3) Parameterized: The constructer will contain parameters, we can pass default values in parameters too.

Constructor Overloading: Constructor overloading is a concept of having more than one constructor with different parameters
                         Python doesn't support constructor overloading.
                         
Constructor Chaining: It's the process of calling one constructor from another constructor.
                      It's convenient when we are dealing with inheritance.
                      
/***************************************************************/
Destructor is a special method that is called when an object gets destroyed.
It is used to perform the clean-up activity before destroying the object, such as closing database connections or filehandle.

Cases when destructor doesn't work correctly
1) In circular referencing occurs when two objects refer to each other.
2) Exception: In OOP, if any exception occurs in the constructor while initializing the object, constructor destroys the object.
"""

# This is an example of constructor chaining
class Vehicle:
    # Constructor of Vehicle
    def __init__(self, engine):
        print('Inside Vehicle Constructor')
        self.engine = engine
        
    # Constructor Overlading
    def __init__(self, engine, make):
        print('Inside Vehicle Constructor')
        self.engine = enginemakeup 

# This is an example of destructor 
class Car(Vehicle):
    # Constructor of Car
    def __init__(self, engine, max_speed):
        super().__init__(engine)
        print('Inside Car Constructor')
        self.max_speed = max_speed
        
    # destructor
    def __del__(self):
        print('Inside destructor')
        print('Object destroyed')

class Electric_Car(Car):
    # Constructor of Electric Car
    def __init__(self, engine, max_speed, km_range):
        super().__init__(engine, max_speed)
        print('Inside Electric Car Constructor')
        self.km_range = km_range

# Object of electric car
ev = Electric_Car('1500cc', 240, 750)
print(f'Engine={ev.engine}, Max Speed={ev.max_speed}, Km range={ev.km_range}')

# calling destructor
dest = Car()
del dest