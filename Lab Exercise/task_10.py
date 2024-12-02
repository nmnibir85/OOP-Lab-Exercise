class Vehicle:
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def vehicle_info(self):
        print(f"Color: {self.__color}")


class Taxi(Vehicle):
    def __init__(self, color, model, capacity, variant):
        super().__init__(color)
        self.__model = model
        self.__capacity = capacity
        self.__variant = variant

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def get_variant(self):
        return self.__variant

    def set_variant(self, variant):
        self.__variant = variant

    def vehicle_info(self):
        super().vehicle_info()
        print(f"Model: {self.__model}")
        print(f"Capacity: {self.__capacity}")
        print(f"Variant: {self.__variant}")


# Create two instances
t1 = Taxi("Red", "Toyota Camry", 4, "Hybrid")
t2 = Taxi("Black", "Honda Civic", 5, "Petrol")

# Access and modify properties
t1.set_model("Toyota Corolla")
t2.set_variant("Diesel")

# Display vehicle information
t1.vehicle_info()
t2.vehicle_info()
