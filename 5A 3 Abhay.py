#F123 ABAHY YADAV

class Engine:
    def __init__(self, power):
        self.power = power


class Car:
    def __init__(self, power):
        self.engine = Engine(power)

    def show(self):
        print("Engine Power:", self.engine.power)


car = Car("2500cc")
car.show()
