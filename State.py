from random import randint
import time

class State:
	def __init__(self):
		self.transition = {}
		self.state = {}
		self.current_state = None
		self.input_response = True
		self.next_state = None
		
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

	def acceptor(self, prompt, valids):
		''' Acceptor style finite state machine to prompt for user input'''
		# als de state geen input vereist (eind state, "refunding" state in dit geval)
		if not valids:
			# dan print de prompt die daarbij hoort en eindig
			print(prompt)
			return ''
		else:	
			# als de state wel input vereist
			while True:
				# maak die input lowercase, check of het geldig is en returneer het
				resp = input(prompt)[0].lower()
				if resp in valids:
					return resp
					
	def finite_state_machine(self, initial_state, exit_state):		
		self.next_state = initial_state
		self.current_state = self.get_state()[self.next_state]

		while self.input_response != exit_state:
			# validate the input
			self.input_response = self.acceptor(self.current_state['prompt'], self.current_state['input_response'])
			# update what the next state will be
			self.next_state = self.get_transition()[self.next_state][self.input_response]

			# als een product wordt afgegeven, printen we dat uit
			if self.next_state == "dispense":
				products = {"1": "Coffee", "2": "Mars", "3": "Chips"}
				print(f"You ordered: {products[self.input_response]}.")

			# update what our current state is
			self.current_state = self.get_state()[self.next_state]