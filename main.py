from State import State
# from StateMachine import StateMachine

if __name__ == "__main__":
	state = State()

	# creating states. 
	# each state has a prompt (message) and an input (required input)
	# first parameter is the state, 2nd is the machine promt and 3rd are the possible inputs
	state.add_state("ready", "Machine ready: (d)eposit money, or (q)uit? ", "['d','q']")
	state.add_state("waiting", "Machine waiting: (s)elect a product, or (r)efund? ", "['s','r']")
	state.add_state("choice", "Which product? (1) Coffee, (2) Mars, (3) Chips, or (r)efund ", "['1', '2', '3', 'r']")
	state.add_state("dispense", "Machine dispensing: please (r)emove product ", "['r']")
	state.add_state("refunding", "Refunding money..", "")
	state.add_state("exit", "", "")	


	# adding transitions
	# each transition links two states with each other, with the input being that link
	# first parameter is the state, 2nd is the input, and 3rd is the next state after receiving given input
	state.add_transition("ready", "d", "waiting")	
	state.add_transition("ready", "q", "exit")	

	state.add_transition("waiting", "s", "choice")	
	state.add_transition("waiting", "r", "refunding")	

	state.add_transition("choice", "1", "dispense")	
	state.add_transition("choice", "2", "dispense")
	state.add_transition("choice", "3", "dispense")	
	state.add_transition("choice", "r", "refunding")	

	state.add_transition("dispense", "r", "ready")	

	state.add_transition("refunding", "", "ready")		


	state.finite_state_machine('ready','q')