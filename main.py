from State import State
# from StateMachine import StateMachine

if __name__ == "__main__":
	state = State()

	# creating states. 
	# each state has a prompt (message) and an input (required input)
	# first parameter is the state, 2nd is the machine promt and 3rd are the possible inputs
	state.add_state("ready", "Machine ready: (d)eposit money, or (q)uit? ", "['d','q']")
	state.add_state("waiting deposit", "Machine waiting: Only these coins/bills are accepted [0.25, 0.5, 1, 2, 5, 10, 20]. Enter (d) when done, (r) to refund or (q)uit ", "['0.25', '0.5', '1', '2', '5', '10', '20', 'd', 'r', 'q']")
	state.add_state("waiting selection", "Machine waiting: (s)elect a product, or (r)efund? ", "['s','r']")
	state.add_state("choice", "Which product? (1) Coffee (€ 0.75), (2) Mars (€ 1.25), (3) Chips (€ 1.50), (r)efund or (d)epost ", "['1', '2', '3', 'r', 'd']")
	state.add_state("dispense", "Machine dispensing: would you like to (p)urchase more or (r)eceive change? ", "['p', 'r']")
	state.add_state("refunding", "", "")
	state.add_state("exit", "", "")	


	# adding transitions
	# each transition links two states with each other, with the input being that link
	# first parameter is the state, 2nd is the input, and 3rd is the next state after receiving given input
	state.add_transition("ready", "d", "waiting deposit")	
	state.add_transition("ready", "q", "exit")	

	state.add_transition("waiting deposit", "0.25", "waiting deposit")
	state.add_transition("waiting deposit",  "0.5", "waiting deposit")
	state.add_transition("waiting deposit",    "1", "waiting deposit")
	state.add_transition("waiting deposit",    "2", "waiting deposit")
	state.add_transition("waiting deposit",    "5", "waiting deposit")
	state.add_transition("waiting deposit",   "10", "waiting deposit")
	state.add_transition("waiting deposit",   "20", "waiting deposit")
	state.add_transition("waiting deposit",   "d",  "waiting selection")
	state.add_transition("waiting deposit",   "r",  "refunding")
	state.add_transition("waiting deposit",   "q",  "refunding")

	state.add_transition("waiting selection", "s", "choice")	
	state.add_transition("waiting selection", "r", "refunding")	

	state.add_transition("choice", "1", "dispense")	
	state.add_transition("choice", "2", "dispense")
	state.add_transition("choice", "3", "dispense")	
	state.add_transition("choice", "r", "refunding")	
	state.add_transition("choice", "d", "waiting deposit")

	state.add_transition("dispense", "r", "refunding")	
	state.add_transition("dispense", "p", "choice")	
	state.add_transition("refunding", "", "ready")		

	state.add_product("1", "0.75")
	state.add_product("2", "1.25")
	state.add_product("3", "1.5")

	# initialiseer de fsm
	state.finite_state_machine('ready','q')