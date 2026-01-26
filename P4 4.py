class Person:
    def __init__(self, name):
        self.name = name

class Majdur(Person):
    def role(self):
        print(self.name, "works as a majdur")

class Labour(Person):
    def role(self):
        print(self.name, "is a labour")

emp = Majdur("Abhay")
emp.role()

a = Labour("Shivam")
a.role()
