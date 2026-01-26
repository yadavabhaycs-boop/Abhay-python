class tata:
    def __init__(self, name):
        self.name = name

class ambuja(tata):
    def show_role(self):
        print(self.name, "is a brand")

a = ambuja("pepsi")
print("Name:", a.name)
a.show_role()
