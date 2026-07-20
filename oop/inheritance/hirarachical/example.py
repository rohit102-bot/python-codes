# One Parent Class
class Animal:
    def eat(self):
        return "Eating food..."

# Child Class 1
class Dog(Animal):
    def bark(self):
        return "Woof!"

# Child Class 2
class Cat(Animal):
    def meow(self):
        return "Meow!"


# Create objects
sparky = Dog()
kitty = Cat()

# Both children can eat (inherited from Animal)
print(sparky.eat())  # Output: Eating food...
print(kitty.eat())   # Output: Eating food...

# Each child has its own unique skill
print(sparky.bark()) # Output: Woof!
print(kitty.meow())  # Output: Meow!
