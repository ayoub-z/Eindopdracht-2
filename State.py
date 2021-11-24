from random import randint
import time

class State:
	def __init__(self):
		self.transition = {}
		self.state = {}
		self.current_state = None
		self.input_response = True
		self.next_state = None
		self.deposit = 0
		self.product = {}
		self.inventory =  {"Coffee": "10", "Mars": "10", "Chips": "10"}
		self.product_list = {"1": "Coffee", "2": "Mars", "3": "Chips"}	

	def add_state(self, state, prompt, input_response):
		# als de state al bestaat, voegen we daar een nieuwe 'promt' en 'input_response' aan toe
		if state in self.state:
			self.state[state]["prompt"] = prompt
			self.state[state]["input_response"] = input_response
		# anders creëren we de state aan en voegen we ze daarna pas
		else: 
			self.state[state] = {}
			self.state[state]["prompt"] = prompt
			self.state[state]["input_response"] = input_response

	def get_state(self):
		return self.state

	def increase_deposit(self, amount):
		self.deposit += float(amount)

	def decrease_deposit(self, amount):
		self.deposit -= float(amount)			

	def get_deposit(self):
		return self.deposit		

	def add_product(self, prod_nm, prod_price):
		self.product[prod_nm] = prod_price

	def get_product(self):
		return self.product

	def update_inventory(self, prod_nm):
		self.inventory[prod_nm] = int(self.inventory[prod_nm]) - 1

	def get_inventory(self):
		return self.inventory

	def add_transition(self, state, input_response, next_state):
		# als de transitie vanuit deze state al bestaat, voegen we hier een nieuwe 'input_response' en de 'next_state' aan toe
		if state in self.transition:
			self.transition[state][input_response] = next_state
		# anders creëren we de transitie en voegen we het daarna pas
		else:
			self.transition[state] = {}
			self.transition[state][input_response] = next_state

	def get_transition(self):
		return self.transition

	def acceptor(self, state, prompt, valids):
		''' Acceptor style finite state machine to prompt for user input'''
		# als de state geen input vereist ("refunding" state in dit geval)
		if not valids:
			# dan print de prompt die daarbij hoort en returneer een lege string. Want het heeft geen input nodig.
			print(prompt)
			return ''
		else:	
			# als de state wel input vereist
			while True:
				if state == "choice":
					resp = input(prompt).lower()
					# check of de input wel geldig is
					if resp in valids:
						if resp == "r" or resp == "d":
							return resp
						# check of er voldoende geld is	
						elif self.get_deposit() - float(self.product[resp])  <= 0:
							print("Not enough deposited. Please pick something cheaper or (d)eposit more..")
							print(f"Current deposited amount: € {self.get_deposit()}\n")
						# check of er voldoende voorraad is	
						elif int(self.get_inventory()[self.product_list[resp]]) <= 0:
							print(f"We've run out of {self.product_list[resp]}. We will try to refill it as soon as possible. Maybe pick another option..\n")
						else:
								return resp
				else:
					resp = input(prompt).lower()
					if resp in valids:
						return resp
					
	def finite_state_machine(self, initial_state, exit_state):		
		self.next_state = initial_state
		self.current_state = self.get_state()[self.next_state]

		while self.input_response != exit_state:
			# de naam van de state waarin we zitten
			current_state_name = (list(self.state.keys())[list(self.state.values()).index(self.current_state)])

			# valideer de input en check of er genoeg voorraad en of er genoeg geld gestort is voor het product
			self.input_response = self.acceptor(current_state_name, self.current_state['prompt'], self.current_state['input_response'])
			# update wat de volgende state zal worden
			self.next_state = self.get_transition()[self.next_state][self.input_response]

			# update deposted amount when money is deposited
			if self.next_state == "waiting deposit" and current_state_name != "ready" and current_state_name != "choice":
				# update 'deposit' wanneer geld gestort is
				self.increase_deposit(self.input_response)
				print("\nCurrent deposited amount: ", self.get_deposit())

			# als een product wordt afgegeven, vermindert zowel de deposit als de voorraad
			elif self.next_state == "dispense":
				# verminder deposit bedrag na uitgave
				self.decrease_deposit(self.product[self.input_response])
				print(f"You ordered: {self.product_list[self.input_response]}.")
				print(f"\nCurrent deposited amount: € {self.get_deposit()}")

				# update inventory (verlaag voorraad van verkocht product met 1)
				self.update_inventory(self.product_list[self.input_response])
				print(f"Remaining amount of {self.product_list[self.input_response]}: {self.get_inventory()[self.product_list[self.input_response]]}")

			# wanneer we geld teruggeven, moet de deposit ook helemaal leeg worden
			elif self.next_state == "refunding":
				# check of er wel geld over is in de deposit
				if self.get_deposit() == 0:
					print(f"Current deposited amount: € {self.get_deposit()}")
					print("Nothing to refund..")
				print(f"\nRefunding: € {self.deposit} ..")
				# verwijder de deposit
				self.decrease_deposit(self.deposit)
				print(f"Current deposited amount: € {self.get_deposit()}")

			# update what our current state is
			self.current_state = self.get_state()[self.next_state]













