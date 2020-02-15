class Product:
    # Constructor
    def __init__(self, name=None, price=0):
        # Object attributes
        self.name = name
        self.price = price

    # Method
    def netPrice(self):
        return  self.price * 1.15


p1 = Product("iPhone 11", 90000)  # Create an object
print(p1.name, p1.price)
print(f"{p1.netPrice():10.2f}")

p2 = Product()
print(p2.name, p2.price)
