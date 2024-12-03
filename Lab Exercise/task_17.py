from abc import ABC, abstractmethod

# Abstract Base Class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def __init__(self):
        print("Car object created.")

    def start(self):
        print("Car engine started.")

    def stop(self):
        print("Car engine stopped.")

class Motorcycle(Vehicle):
    def __init__(self):
        print("Motorcycle object created.")

    def start(self):
        print("Motorcycle engine started.")

    def stop(self):
        print("Motorcycle engine stopped.")

# Create an object of Car
car = Car()
car.start()
car.stop()

# Attempting to create an object of Vehicle (Raises TypeError)
# vehicle = Vehicle()  # Uncomment to see the error
