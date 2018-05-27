'''code for question 4'''

def readRecord():
	pass

def computeRegular(minutes):
	threshold = 50
	pay1 = 10.00
	pay2 = 0.20
	if minutes <= threshold:
		return pay1
	else:
		return pay1 + (minutes - threshold)*pay2


def computePremium(daytime,offpeak):
	pass

def printrecord():
	pass

def main():
	pass

if __name__ == "__main__":
	main()