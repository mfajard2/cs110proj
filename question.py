class ynquestions:    
	def __init__(self):
		self.qs=["Do you smoke?", "Do you consider yourself a light sleeper?","Do you have and/or want pets?", "Do you mind if your roommate has frequent overnight guests?", "Are you willing to split the grocery bill?", "Are you willing to split chores in a shared living space?","Do you have any dietary restrictions, be it from allergies or personal choice? ", "Do you mind if your roommate has frequent daytime guests if they leave at a time you find appropriate?"]

class fill_in:
	def __init__(self):
		self.fq= ["Full Name","Gender","What state are you from?(Please enter state abbreviation", "Age", "Leave a a personal message or a short description of yourself"]

class multquestions:
	def __init__(self):
		self.mq= ["At about what hour do you go to sleep?", "At about what hour do you wake up?", "If you workout, how often do you do so?", "Which one best describes you?", "Which do you prefer?", "Living preference?", "How much are you looking to spend on rent, including utilities, per month?"]

class mult_answr:
	def __init__(self):
		self.ma=[("9-10","11-12", "past midnight"),("before 8", "8-10", "10-12", "afternoon"),("very often", "moderately", "on occasion", "never"), ("complete mess", "sometimes messy but relatively organized", "pretty tidy", "neat freak"),("quiet living space", "noisy living space", "some combination of the two"),("near a big city", "suburbs", "rural area"),("200-400", "400-600", "600-800", "800+")]


'''class multquestions:
	def __init__(self):
		self.mq= [["At about what hour do you go to sleep?","9-10","11-12", "past midnight"], ["At about what hour do you wake up?","before 8", "8-10", "10-12", "afternoon"], "If you workout, how often do you do so?","very often", "moderately", "on occasion", "never"], "Which one best describes you?","complete mess", "sometimes messy but relatively organized", "pretty tidy", "neat freak"], "Which do you prefer?","quiet living space", "noisy living space", "some combination of the two"], "Living preference?","near a big city", "suburbs", "rural area"], "How much are you looking to spend on rent, including utilities, per month?","200-400", "400-600", "600-800", "800+"]]'''





	def num_match(self, match):
		num=0
		if(self.qs[1]== match.q1):
			num +=25
		else: 
			num+=0
		if(self.q2== match.q2):
			num +=1
		else:
			num+=0
		if(self.q3== match.q3):
			num +=5
		else:
			num+=0
		if(self.q4== match.q4):
			num +=5
		else:
			num+=0
		if(self.q5== match.q5):
			num +=1
		else:
			num+=0
		if(self.q6== match.q6):
			num +=1	
		else:
			num+=0
		if(self.q7== match.q7):
			num +=1
		else:
			num+=0
		if(self.q8== match.q8):
			num +=3
		else:
			num+=0
		if(self.q9== match.q9):
			num +=3
		else:
			num+=0
		if(self.q10== match.q10):
			num +=1
		else:
			num+=0
		if(self.q11== match.q11):
			num +=1
		else:
			num+=0
		if(self.q12== match.q12):
			num +=1
		else:
			num+=0
		if(self.q13== match.q13):
			num +=3
		else:
			num+=0
		if(self.q14== match.q14):
			num +=25
		else:
			num+=0
		if(self.q15== match.q15):
			num +=25
		else:
			num+=0

		return num + "% Match"

