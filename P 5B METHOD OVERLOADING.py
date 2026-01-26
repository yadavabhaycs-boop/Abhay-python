class Animal:
    def make_sound(self):
        return "some generic sound"

class Dog(Animal):
    def make_sound(self):
        return "woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

dog = Dog()
cat = Cat()

print(dog.make_sound())
print(cat.make_sound())
