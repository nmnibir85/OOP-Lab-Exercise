import numpy as np

# 1. Create a NumPy array
score = np.array([85, 90, 78, 97, 88])
# a) Convert data type to float
score_float = score.astype(float)
print("Score (float):", score_float)
# b) Create a copy and add 5 points
score_copy = score.copy() + 5
print("Score copy:", score_copy)
# c) Find array properties
print("Shape:", score.shape)
print("Dimension:", score.ndim)
print("Size:", score.size)
print("Item size:", score.itemsize)
print("Data type:", score.dtype)
print("Sorted score:", np.sort(score))
# d) Find indices with scores >= 80
indices = np.where(score >= 80)
print("Indices with scores >= 80:", indices)
# e) Find min, max, std, var, sum, mean, axis-wise mean
print("Min:", np.min(score))
print("Max:", np.max(score))
print("Standard deviation:", np.std(score))
print("Variance:", np.var(score))
print("Sum:", np.sum(score))
print("Mean:", np.mean(score))
print("Axis-wise mean:", np.mean(score, axis=0))
# f) Print specific elements and slices
print("Score[2]:", score[2])
print("Score[-3:]:", score[-3:])
print("Score[1:4]:", score[1:4])
TASK - 1
Let
's break down the class diagram into two tasks:
Task
1:
• We
have
an
abstract


class Vehicle with two methods: start() and stop().

• Two
concrete
classes
Car and Motorcycle
inherit
from Vehicle.

Task
2:
• The
Vehicle


class is now modified with additional attributes: brand and description.

• The
startEngine()
method is made
abstract.
Python
Implementation


class Vehicle:
    def start(self):

        pass


def stop(self):
    pass


class Car(Vehicle):
    def __init__(self):

        pass


class Motorcycle(Vehicle):
    def __init__(self):
        pass

    # Create an object of Car


car = Car()

# Create an object of Vehicle (This will raise an error)
vehicle = Vehicle()  # TypeError: Can't instantiate abstract class Vehicle with abstract methods
startEngine
TASK - 2


class Vehicle:
    def __init__(self, brand, description):
        self.brand = brand
        self.description = description

    def startEngine(self):
        raise NotImplementedError("Subclasses must implement this method")

    def stopEngine(self):
        pass


class Car(Vehicle):
    def __init__(self, brand, model, description):
        super().__init__(brand, description)


self.model = model


def startEngine(self):
    print(f"Starting {self.brand} {self.model}")


# Create an object of Car
car = Car("Toyota", "Camry", "A comfortable sedan")
car.startEngine()  # Output: Starting Toyota Camry
# Create an object of Vehicle (This will raise an error)
vehicle = Vehicle("Unknown", "Unknown")  # TypeError: Can't instantiate abstract class Vehicle with
abstract
methods
startEngine