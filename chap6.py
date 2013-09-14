# Enter your answrs for chapter 6 here
# Name: Ethan Puzarne

import string

# Ex. 6.6
def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

# 6.6-1
# middle on string with 2 letters:
# empty string

# middle on one letter
# empty string

# middle on empty string
# empty string



# 6.6-2
def is_palindrome(given_string):
	''' Takes a string and recursively determines if it is a palindrome
	while ignoring punctuation '''
	# somewhat redundant given that it only needs to remove punctuation once
	given_string = given_string.lower().replace(" ", "")
	stripped = given_string.translate(string.maketrans("",""), string.punctuation)
	if len(stripped) <= 1:
		return True
	elif first(stripped) == last(stripped):
		return is_palindrome(middle(stripped))
	else:
		return False

# Tests
print(is_palindrome("palindrome") == False)
print(is_palindrome("racecar") == True)
print(is_palindrome("little miss susie went to market") == False)
print(is_palindrome("Never odd or even") == True)
print(is_palindrome("Doc, note: I dissent. A fast never prevents a fatness. I diet on cod") == True)



# Ex 6.8
def gcd(numA, numB):
	''' Return greatest common divisor of two numbers '''
	try:
		numA,numB = int(numA),int(numB)
	except ValueError:
		return None

	if numA % numB == 0:
		return numB
	elif numB % numA == 0:
		return numA
	elif numA < numB:
		return gcd(numA, numB % numA)
	elif numA > numB:
		return gcd(numA % numB, numB)

print("Test Passed" if gcd(50,90)==10 else "Test Failed")
print("Test Passed" if gcd(256, 256)==256 else "Test Failed")
print("Test Passed" if gcd(1024,256)==256 else "Test Failed")
print("Test Passed" if gcd(75,50)==25 else "Test Failed")