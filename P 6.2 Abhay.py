from abc import ABC, abstractmethod

# Abstract Class with Abstract Method
class Car(ABC):

    @abstractmethod
    def car_type(self):
        pass


# BMW class
class BMW(Car):
    def car_type(self):
        print("BMW is a luxury sports car")


# Bugatti F123 class
class BugattiF123(Car):
    def car_type(self):
        print("Bugatti F123 is a hyper sports car")


# Macaron class
class Macaron(Car):
    def car_type(self):
        print("Macaron is a high-performance hybrid car")


# Range Rover class
class RangeRover(Car):
    def car_type(self):
        print("Range Rover is a luxury SUV")


# Object creation
cars = [BMW(), BugattiF123(), Macaron(), RangeRover()]

for car in cars:
    car.car_type()
