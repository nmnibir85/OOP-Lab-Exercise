class Shape:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def display_info(self):
        print(f"Shape: {self.name}")


class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_detail(self):
        print(f"Name: {self.name}, Price: {self.price}")


class ElectronicProduct(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def display_detail(self):
        super().display_detail()
        print(f"Warranty: {self.warranty}")


# Creating objects
rectangle = Rectangle("Rectangle", 5, 4)
rectangle.display_info()
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")

electronic_product = ElectronicProduct("Laptop", 1000, "1 year")
electronic_product.display_detail()
