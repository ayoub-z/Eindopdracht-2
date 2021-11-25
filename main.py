from VendingMachine import VendingMachine
from Product import Product
import random


if __name__ == "__main__":
	vending_machine = VendingMachine()

	mars = Product('Mars', 2.0)
	red_bull = Product('Red Bull', 2.5)
	twix = Product('Twix', 1.5)
	cola = Product('Cola', 2.2)
	chips = Product('Chips', 1.4)

	vending_machine.add_product(mars)
	vending_machine.add_product(red_bull)
	vending_machine.add_product(twix)
	vending_machine.add_product(cola)
	vending_machine.add_product(chips)

	vending_machine.run(3.0, [mars])
	vending_machine.run(4.0, [mars])
	vending_machine.run(10.0, [mars, twix, red_bull])
	vending_machine.run(5.0, [mars, twix, red_bull])
	vending_machine.run(4.0, [mars, red_bull])
	vending_machine.run(7.0, [mars, twix, red_bull])

	"""
	Voor meerdere dagen worden een random aantal personen gekozen tussen 0 en 50.
	Voor elk van deze personen worden een bedrag van 2 tot 10 euro gekozen en hoeveel producten de persoon wil kopen (tussen 1 en 3).
	Hieronder wordt een simulatie gedraaid van 10 dagen.
	"""
	for dag in range(10):
		persons = random.randrange(50)
		for i in range(persons):
			money = random.randrange(20, 100) / 10
			product_rand = random.randrange(1, 4)
			rand_products = random.sample(vending_machine.products, product_rand)

			vending_machine.run(money, rand_products)

		vending_machine.refill_product_stock()
