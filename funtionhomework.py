# author: joshsanyal

def isGreaterThan100(n):
	if 100 > n:
		return True
	else:
		return False

def whichIsGreater(a, b):
	if a > b:
		return a
	else:
		return b
	
def whichIsGreater(a, b, c):
	if a > b + a > c:
		return a
	if b > a + b > c:
		return b
	if c > b + c > b:
		return c
	
def whichIsSmaller(a, b, c):
	if a < b + a < c:
		return a
	if b < a + b < c:
		return b
	if c < b + c < b:
		return c

# Return whether a is divisible by b

def divisibleBy(a, b):
	if a / b == % range(b - 1) == 0:
		return True
	else:
		return False

# Simple functions, shouldn't take you more than 15 seconds

def add(a, b):
	total = 0
	total = total + a + b

def subtract(a, b):
	total = 0
	total = total + a - b

def multiply(a, b):
	total = 0
	total = total + a * b

def divide(a, b):
	total = 0
	total = total + a / b

#interesting function: a to the power of b

def power(a, b):
	total = 0
	total = total + a

def absoluteValue(a):
	return a

# challenge functions

# hint - use the modulus and division

def palindromeNumber(n):
	return alse

def sumOfDigits(n):
	return 0