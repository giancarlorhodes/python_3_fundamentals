
# understanding scope
def _name_func(name = 'Mark'):
    print("name parameter is: ", name)

    
name = input("Enter your name: ")
print("(Global) Your name is ", name)
_name_func()

# the game is called Hus'lin
class Person:

    def __init__(self, inName):
        self.name = inName
        self.points = 0

    def GetPoints(self):
        return self.points
    
    def SetPoints(self, inPoints):
        self.points = inPoints


class Pimp(Person):

    def __init__(self, inName):
        #add properties etc.
        #self.name = inName # local class properties name which is not what you want, use the parent class property
        super().__init__(inName)


class Worker(Person):

    def __init__(self, inName):
        super().__init__(inName)
        #self.name = inName
    
    
class Customer(Person):

     def __init__(self, inName):
        super().__init__(inName)


class Police(Person):

     def __init__(self, inName):
        super().__init__(inName)


