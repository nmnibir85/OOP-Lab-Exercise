# Base class with methods to be implemented by subclasses
class Vehicle:
    def __init__(self, brand, description):
        self.brand = brand
        self.description = description

    def startEngine(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def stopEngine(self):
        print("Engine stopped.")

class Car(Vehicle):
    def __init__(self, brand, model, description):
        super().__init__(brand, description)
        self.model = model

    def startEngine(self):
        print(f"Starting {self.brand} {self.model}")

# Create an object of Car
car = Car("Toyota", "Camry", "A comfortable sedan")
car.startEngine()  # Output: Starting Toyota Camry

# Attempting to create an object of Vehicle (Raises NotImplementedError if startEngine is called)
try:
    vehicle = Vehicle("Unknown", "Unknown")
    vehicle.startEngine()  # Uncomment this line to see the NotImplementedError
except NotImplementedError as e:
    print(f"Error: {e}")
