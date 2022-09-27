"""
Encapsulation
Encapsulation is used to bundle data members and methids within a single unit, a fine example of encapsulation is class().

There are three access modifiers
1) Public: Public variable can be accessed anywhere in the code
2) Protected: Protected variable can be accessed within the class and sub-class.
3) Private: Private variable can only be accessed within a class.

Advantages of encapsulation
1) Security: The main advantage of using encapsulation is the security of the data. Encapsulation protects an object from unauthorized access.
2) Data Hiding: The user would not know what's going behind the scene. They will only be knowing that to modify a data member,
call the setter method. To read a data member, call the getter method. What these setter and getter methods are doing is hidden from them.
3) Simplicity: It simplifies the maintenance of the application by keeping classes separated and preventing them from tightly coupling with each other.
4) Aesthetics: Bundling data and methods within a class makes code more readable and maintainable
"""
class Aladdin():
    x = 1
    def __init__(self, name, age, gender):
        self.name = name
        self._age = age # This is a private variable
        self.__gender = gender # This is a protected variable
        
    def nothing(self):
        print(self.__gender)
        
    @classmethod
    def something(cls, y):
        cls.x = y
    
a =  Aladdin("Salam", 19, "M")

a.name
a._age # calling Protected instance
a._Aladdin__gender # name mangling method

a.nothing() # calling a method with  

a.something(6)
a.x
