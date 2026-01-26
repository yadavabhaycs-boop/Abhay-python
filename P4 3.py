class student:
    def __init__(self, name):
        self.name = name

class name(student):
    def show_role(self):
        print(self.name, "is a name")

class roll1(name):
    def teacher(self, t):
        print(self.name, "class", t)

r = roll1("Abhay")
r.show_role()
r.teacher("topper")
