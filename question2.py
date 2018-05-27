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
	guess = input("Guess a number between 0 and 99: ")

if __name__ == "__main__":
	main()