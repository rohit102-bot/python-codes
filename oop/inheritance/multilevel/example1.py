class Organism:
    def Alive(self):
        return True
    
class Animal(Organism):
    def Dog(self):
        print("dog is barking")

class Birds(Animal):
    def sing(self):
        print("bird is singing")

b=Birds()
b.sing()
b.Dog()
print(b.Alive())