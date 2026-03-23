class Bird:
    def sound(self):
        print("Bird sound")

class Sparrow(Bird):
    def sound(self):
        print("Chirp")

class Crow(Bird):
    def sound(self):
        print("Caw")

for b in [Sparrow(), Crow()]:
    b.sound()