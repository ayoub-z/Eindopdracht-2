class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.stock = 50

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_stock(self):
        return self.stock

    def decrease_stock(self):
        self.stock -= 1

    def set_stock(self, number):
        self.stock = number
