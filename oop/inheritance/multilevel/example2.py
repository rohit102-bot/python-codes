# Grandparent Class
class Animal:

    def eat(self):
        return "Eating food..."


# Parent Class
class Dog(Animal):

    def bark(self):
        return "Woof! Woof!"


# Child Class
class Puppy(Dog):

    def weep(self):
        return "Whining..."


# Create a Puppy object
my_puppy = Puppy()

# The puppy can do everything its parents and grandparents can do
print(my_puppy.eat())  # From Animal (Grandparent)
print(my_puppy.bark())  # From Dog (Parent)
print(my_puppy.weep())  # From Puppy (Itself)
