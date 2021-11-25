from VendingMachine import VendingMachine
from Product import Product

if __name__ == "__main__":
	vending_machine = VendingMachine()

	mars = Product('Mars', 2.0, 10)
	red_bull = Product('Red Bull', 2.5, 20)
	twix = Product('Twix', 1.5, 15)
	cola = Product('Cola', 2.2, 20)
	chips = Product('Chips', 1.4, 10)

	vending_machine.run(3.0, [mars])
	vending_machine.run(4.0, [mars])
	vending_machine.run(10.0, [mars, twix, red_bull])
	vending_machine.run(5.0, [mars, twix, red_bull])
	vending_machine.run(4.0, [mars, red_bull])
	vending_machine.run(7.0, [mars, twix, red_bull])
