'''code for question 1'''

def search(str,lst,size):
	pos = 0
	result = -1
	for i in range(0,size):
		if str == lst[i]:
			result = pos
		else:
			pos += 1
	return result



if __name__ == "__main__":
	main()