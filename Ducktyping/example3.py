class Dog:
    def speak(self):
        print("Bark")

class Robot:
    def speak(self):
        print("Beep Beep")

def make_sound(obj):
    obj.speak()

d = Dog()
r = Robot()

make_sound(d)
make_sound(r)