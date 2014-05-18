# author: joshsanyal

def isPrime(n):
	tests = range(2, n / 2 + 1)
	for test in tests:
		if n % test == 0:
			return False
		
	return True

for n in range(2,1000):
	if isPrime(n) and isPrime(n + 2):
		print str(n) + " and " + str(n + 2)