import abc 
class Animal(abc.ABC):
    @abc.abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("barking")

class cat(Animal):
    def sound(self):
        print("meow")

c=cat()
d=Dog()
d.sound()    
c.sound()
