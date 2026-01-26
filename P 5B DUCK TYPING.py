class Duck:
    def sound(self):
        print("Quack!")

class Person:
    def sound(self):
        print("I'm quacking like a duck!")

def make_it_sound(obj):
    obj.sound()

# Using the Duck class
d = Duck()
make_it_sound(d)

# Using the Person class
p = Person()
make_it_sound(p)

