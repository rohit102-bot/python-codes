# Grandparent class
class Vehicle:
    def start(self):
        return "Engine started"

# Parent 1 (Single inheritance from Vehicle)
class Car(Vehicle):
    def drive(self):
        return "Driving on land"

# Parent 2 (Single inheritance from Vehicle)
class Boat(Vehicle):
    def sail(self):
        return "Sailing on water"

# Child class (Multiple inheritance from Car and Boat)
# This completes the hybrid structure
class AmphibiousCar(Car, Boat):
    pass

# Create object
monster_truck = AmphibiousCar()

# It can do everything
print(monster_truck.start())  # Output: Engine started
print(monster_truck.drive())  # Output: Driving on land
print(monster_truck.sail())   # Output: Sailing on water
