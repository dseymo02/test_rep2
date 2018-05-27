'''code for question 2'''

def check(number,guess):
	if guess < number:
		return "Too low"
	elif guess > number:
		return "Too high"
	else:
		return "Correct"