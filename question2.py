'''code for question 2'''
from random import randint

def check(number,guess):
	if guess < number:
		return "Too low"
	elif guess > number:
		return "Too high"
	else:
		return "Correct"

def main():
	count = 0
	number = randint(0,99)
	guess = input("Guess a number between 0 and 99: ")
	finished = False
	while not finished:
		count += 1
		if guess < number:
			guess = input("Too low, Guess again: ")
		elif guess > number:
			guess = input("Too high, Guess again: ")
		else:
			finished = True
	print("Correct. It took you, ",count," guesses")

if __name__ == "__main__":
	main()