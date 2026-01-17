from abc import ABC, abstractmethod

# Interface (Only abstract methods)
class CarInterface(ABC):

    @abstractmethod
    def engine(self):
        pass

    @abstractmethod
    def speed(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass


# BMW implements interface
class BMW(CarInterface):
    def engine(self):
        print("BMW uses a turbo engine")

    def speed(self):
        print("BMW top speed is 250 km/h")

    def fuel_type(self):
        print("BMW uses petrol")


# Bugatti F123 implements interface
class BugattiF123(CarInterface):
    def engine(self):
        print("Bugatti F123 uses a W16 engine")

    def speed(self):
        print("Bugatti F123 top speed is 420 km/h")

    def fuel_type(self):
        print("Bugatti F123 uses petrol")


# Macaron implements interface
class Macaron(CarInterface):
    def engine(self):
        print("Macaron uses a hybrid engine")

    def speed(self):
        print("Macaron top speed is 350 km/h")

    def fuel_type(self):
        print("Macaron uses electric + petrol")


# Range Rover implements interface
class RangeRover(CarInterface):
    def engine(self):
        print("Range Rover uses a V8 engine")

    def speed(self):
        print("Range Rover top speed is 210 km/h")

    def fuel_type(self):
        print("Range Rover uses diesel")


# Object creation
cars = [BMW(), BugattiF123(), Macaron(), RangeRover()]

for car in cars:
    car.engine()
    car.speed()
    car.fuel_type()
    print("------")
