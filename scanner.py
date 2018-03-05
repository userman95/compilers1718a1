
def getchar(words,pos):
	""" returns char at pos of words, or None if out of bounds """

	if pos<0 or pos>=len(words): return None

	return words[pos]
	

def scan(text,transition_table,accept_states):
	""" Scans `text` while transitions exist in 'transition_table'.
	After that, if in a state belonging to `accept_states`,
	returns the corresponding token, else ERROR_TOKEN.
	"""
	
	# initial state
	pos = 0
	state = 'q0'
	
	while True:
		
		c = getchar(text,pos)	# get next char
		
		if state in transition_table and c in transition_table[state]:
		
			state = transition_table[state][c]	# set new state
			pos += 1	# advance to next char
			
		else:	# no transition found

			# check if current state is accepting
			if state in accept_states:
				return accept_states[state],pos

			# current state is not accepting
			return 'ERROR_TOKEN',pos
			
	
# the transition table, as a dictionary

# Αντικαταστήστε με το δικό σας λεξικό μεταβάσεων...
td = { 'q0':{ 't':'q1','l':'q2' },
       'q1':{ 'e':'q3' },
       'q2':{ 'o':'q8' },
       'q3':{ 's':'q4','r':'q6' },
       'q4':{ 't':'q5' },
       'q6':{ 'm':'q7' },
       'q8':{ 'n':'q9' },
       'q9':{ 'g':'q10'}
     } 

# the dictionary of accepting states and their
# corresponding token

# Αντικαταστήστε με το δικό σας λεξικό καταστάσεων αποδοχής...
ad = { 'q5':'TEST_TOKEN',
       'q7':'TERM_TOKEN',
       'q10':'LONG_TOKEN'
     }


# get a string from input
text = input('give some input>')

# scan text until no more input
while text:	# that is, while len(text)>0
	
	# get next token and position after last char recognized
	token,position = scan(text,td,ad)
	
	if token=='ERROR_TOKEN':
		print('unrecognized input at pos',position+1,'of',text)
		break
	
	print("token:",token,"string:",text[:position])
	
	# remaining text for next scan
	text = text[position:]
	
