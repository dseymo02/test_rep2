from question1 import *
from question2 import *
from question3 import *
from question4 import *
import pytest

def search():
	string = "hello"
	lst = ["hi","holla","hello","bon day"]
	size = len(lst)
	assert search(string, lst, size) == 2