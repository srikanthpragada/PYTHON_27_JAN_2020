class Product:
    # class attributes (static variable)
    taxrate = 15

    @staticmethod
    def price_after_tax(price):
        return  price + price * Product.taxrate / 100

    # Constructor
    def __init__(self, name=None, price=0):
        # Object attributes
        self.name = name
        self.price = price
        self.taxrate = 15

    # Method
    def netPrice(self):
        return self.price * Product.taxrate / 100 + self.price


print("50000 after tax = ", Product.price_after_tax(50000))

p1 = Product("iPhone 11", 100000)  # Create an object
print(p1.name, p1.price)
print(f"{p1.netPrice():10.2f}")

p2 = Product()
print(p2.name, p2.price)
