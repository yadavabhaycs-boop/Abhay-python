class animals:
    def __init__(self, name):
        self.name = name

class lion:
    def __init__(self, species):
        self.species = species

class mouse(animals, lion):
    def __init__(self, name, species):
        animals.__init__(self, name)
        lion.__init__(self, species)

    def details(self):
        print(self.name, "types", self.species)

m = mouse("jerry", 100)
m.details()
