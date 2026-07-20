# Parent 1
class Camera:
    def take_photo(self):
        return "📸 Photo taken!"

# Parent 2
class Radio:
    def play_music(self):
        return "📻 Playing music!"

# Child class combines both
class Smartphone(Camera, Radio):
    pass  # 'pass' means this class is empty for now


# Create a phone object
my_phone = Smartphone()

# The phone can do everything both parents can do
print(my_phone.take_photo())  # Output: 📸 Photo taken!
print(my_phone.play_music())  # Output: 📻 Playing music!
