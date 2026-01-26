class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("My name is", self.name)
        print("My age is", self.age)

    def greet(self):
        print("Name:", self.name)
        print("Age:", self.age)

p = person("Abhay", 20)
p.greet()
