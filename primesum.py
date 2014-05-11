# author: joshsanyal
# 1. Average distance
# 2. Largest distance
# 3. Smallest distance
# 4. How many twin primes
# 5. Sum of the distance between twin primes

total = 0
lastPrime = 2
numbers = range(2,1001)
for n in numbers:
	tests = range(2,n-1)
	prime = True
	for t in tests:
		if n % t == 0:
			prime = False
	if prime:
		total = total + ( n - lastPrime)
		lastPrime = n	
print total