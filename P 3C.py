a = 10
b = 20

class MyClass:
    def add_numbers(self):
        result = a + b
        print("Sum =", result)

    def compare_numbers(self):
        if a > b:
            print("a is greater than b")
        else:
            print("b is greater than or equal to a")

obj = MyClass()
obj.add_numbers()
obj.compare_numbers()
