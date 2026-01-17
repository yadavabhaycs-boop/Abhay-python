#F123 ABHAY YADAV%

class A:
    def __init__(self, x):
        self.x = x


class B:
    def display(self, value):
        print("MUNAFA HUA:", value)


objA = A(10)

objB = B()

objB.display(objA.x)
