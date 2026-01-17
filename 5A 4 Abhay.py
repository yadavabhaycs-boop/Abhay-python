#F123 ABHAY YADAV
class Outer:
    def __init__(self):
        self.msg = "Hello from Outer class"

    class Inner:
        def __init__(self, outer_obj):
            self.outer_obj = outer_obj

        def show(self):
            print(self.outer_obj.msg)


outer = Outer()
inner = outer.Inner(outer)
inner.show()
