class Person:
    class Adress:#Innner class/memeber class
        def __init__(self):
            self.__hno=None
            self.__street=None
            self.__city=None
        def readAdress(self):
            self.__hno=input("houseno: ")
            self.__street=input("Street: ")
            self.__city=input("city:")
        def printAdress(self):
            print(f"{self.__hno},{self.__street},{self.__city}")

    def __init__(self):
        self.__name=None
        self.__add=Person.Adress()
    def readPerson(self):
        self.__name=input("Name: ")
        self.__add.readAdress()
    def printPerson(self):
        print(f"{self.__name}")
        self.__add.printAdress()

p1=Person()
p1.readPerson()
p1.printPerson()
