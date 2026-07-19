class Address:
    def __init__(self):
        self.__street=None
        self.__city=None

    def readAddress(self):
        self.__street=input("street:")
        self.__city=input("ciyt:")
    
    def printAddress(self):
        print(f"{self.__street}  {self.__city}")
    

class Person:
    def __init__(self):
        self.__name=None
        self.__add=Address()
    def readPerson(self):
        self.__name=input("enter the name:")
        self.__add.readAddress()
    def printPerson(self):
        print(f"{self.__name}")
        self.__add.printAddress()

p1=Person()
p1.readPerson()
p1.printPerson()