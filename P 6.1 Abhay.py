from abc import ABC, abstractmethod

# Abstract Class
class Car(ABC):

    @abstractmethod
    def engine(self):
        pass

    @abstractmethod
    def top_speed(self):
        pass


# Child Class 1
class BMW(Car):
    def engine(self):
        print("BMW uses a turbocharged engine")

    def top_speed(self):
        print("BMW top speed is 250 km/h")


# Child Class 2
class BugattiF123(Car):
    def engine(self):
        print("Bugatti F123 uses a W16 engine")

    def top_speed(self):
        print("Bugatti F123 top speed is 420 km/h")


# Child Class 3
class Macaron(Car):
    def engine(self):
        print("Macaron uses a hybrid engine")

    def top_speed(self):
        print("Macaron top speed is 350 km/h")


# Child Class 4
class RangeRover(Car):
    def engine(self):
        print("Range Rover uses a V8 engine")

    def top_speed(self):
        print("Range Rover top speed is 210 km/h")


# Object Creation
cars = [BMW(), BugattiF123(), Macaron(), RangeRover()]

for car in cars:
    car.engine()
    car.top_speed()
    print("------")
5
