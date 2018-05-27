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
	basecharge = 25.00
	daytimethreshold = 75
	pay1 = 0.10
	offpeakthreshold = 100
	pay2 = 0.05
	total = basecharge
	if daytime > daytimethreshold:
		total = total + (daytime - daytimethreshold)*pay1
	if offpeak > offpeakthreshold:
		total = total + (offpeak - offpeakthreshold)*pay2
	return total 

def printrecord():
	pass

def main():
	pass

if __name__ == "__main__":
	main()