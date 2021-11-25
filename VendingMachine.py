class VendingMachine:
    def __init__(self):
        self.ready_for_coins = True
        self.deposit = 0
        self.products = []

    def change_ready_state(self):
        if self.ready_for_coins:
            self.ready_for_coins = False
        else:
            self.ready_for_coins = True

    def get_ready_for_coins(self):
        return self.ready_for_coins

    def get_deposit(self):
        return self.deposit

    def increase_deposit(self, amount):
        self.deposit += float(amount)

    def decrease_deposit(self, amount):
        self.deposit -= float(amount)

    def refund_deposit(self):
        self.deposit = 0

    def get_products(self):
        return self.products

    def add_product(self, product):
        self.products.append(product)

    def run(self, deposit, products):
        print("Machine ready, deposit coins")
        self.increase_deposit(deposit)

        for product in products:
            if product.get_price() <= self.deposit:
                print(f"Coins inserted {self.deposit} euro")
                self.change_ready_state()
                if product.get_stock() > 0:
                    product.decrease_stock()
                    self.decrease_deposit(product.get_price())
                    print(f"Despensing {product.get_name()}")

                    self.change_ready_state()
                else:
                    print("unfortunately the product is out of stock")

            else:
                print(f"Not enough money for {product.get_name()}")
                break

        print(f"Refunding {self.deposit} euro\n")
        self.refund_deposit()