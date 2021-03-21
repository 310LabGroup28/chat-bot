from random import randrange

class OutOfScope(object):
	def getResponse():
		randomNum = randrange(5)
		if randomNum == 0:
			return "I'm sorry, I didn't quite understand that.\nTry asking for help to see the scope of my functionality, or try asking another question.\n"
		elif randomNum == 1:
			return "It appears your question is out of scope, please try asking something else.\n"
		elif randomNum == 2:
			return "Whoops! I don't understand that!\n"
		elif randomNum == 3:
			return "I didn't catch that. If you believe I should have understood your question, try rephrasing it!\n"
		else:
			return "I'm confused, try asking something else.\n"