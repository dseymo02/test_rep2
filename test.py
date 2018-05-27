from question1 import *
from question2 import *
from question3 import *
from question4 import *
import pytest

# testing for question 1
def testsearch():
	string = "hello"
	string2 = "ella"
	lst = ["hi","holla","hello","bon day"]
	size = len(lst)
	assert search(string, lst, size) == 2
	assert search(string2, lst, size) == -1

# testing for question 2

def testcheck():
	number = 70
	guess1 = 50
	guess2 = 80
	guess3 = 70
	assert check(number,guess1) == "Too low"
	assert check(number,guess2) =="Too high"
	assert check(number, guess3) =="Correct"

# testing for question 3

def testsqrProd():
	a = 2
	b = 5
	assert sqrProd(a,b) == 100

# testing for question 4

def testComputeRegular():
	minutes = 55
	assert computeRegular(minutes) == 11.00

def testComputePremium():
	daytime = 0
	offpeak = 139
	assert computePremium(daytime,offpeak) == 26.95