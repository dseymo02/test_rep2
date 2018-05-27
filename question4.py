'''code for question 4'''

def readRecord():
	record = []
	str = input()
	record = str.split()
	return record


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
	finished = False
	records = []
	terminate = 'X0000'
	while not finished:
		record = readRecord()
		if record[0] == terminate:
			record.pop(0)
			finished = True
			break
		records.append(record)
	size = len(records)
	charges = []
	for n in records:
		if n[3] == "R":
			minutes = n[4]
			charge = computeRegular(minutes)
			charges.append(charge)
		else:
			daytime = n[4]
			offpeak = n[5]
			charge = computePremium(daytime,offpeak)
			charges.append(charge)
	print(charges)


if __name__ == "__main__":
	main()