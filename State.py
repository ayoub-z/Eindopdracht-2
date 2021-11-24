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
		if state in self.state:
			self.state[state]["prompt"] = prompt
			self.state[state]["input_response"] = input_response
		else: 
			self.state[state] = {}
			self.state[state]["prompt"] = prompt
			self.state[state]["input_response"] = input_response

	def get_state(self):
		return self.state

	def add_transition(self, state, input_response, transition):
		if state in self.transition:
			self.transition[state][input_response] = transition
		else:
			self.transition[state] = {}
			self.transition[state][input_response] = transition

	def get_transition(self):
		return self.transition

	def acceptor(self, prompt, valids):
		''' Acceptor style finite state machine to prompt for user input'''
		if not valids: 
			print(prompt)
			return ''
		else:	
			while True:
				resp = input(prompt)[0].lower()
				if resp in valids:
					return resp
					
	def finite_state_machine(self, initial_state, exit_state):		
		self.next_state = initial_state
		self.current_state = self.get_state()[self.next_state]

		while self.input_response != exit_state:
			self.input_response = self.acceptor(self.current_state['prompt'], self.current_state['input_response'])
			self.next_state = self.get_transition()[self.next_state][self.input_response]

			# als een product wordt afgegeven, printen we dat uit
			if self.next_state == "dispense":
				products = {"1": "Coffee", "2": "Mars", "3": "Chips"}
				print(f"You ordered: {products[self.input_response]}.")
			self.current_state = self.get_state()[self.next_state]