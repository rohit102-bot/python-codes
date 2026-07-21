# Parent Class
class Animal:
    def make_sound(self):
        print("Some generic animal sound")

# Child Class inheriting from Animal
class Dog(Animal):
    # Overriding the parent class method
    def make_sound(self):
        print("Bark! Bark!")

# --- Execution ---

# Instance of the parent class
generic_animal = Animal()
generic_animal.make_sound()  # Output: Some generic animal sound

# Instance of the child class
my_dog = Dog()
my_dog.make_sound()          # Output: Bark! Bark!
