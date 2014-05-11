# author: joshsanyal
numbers = range(2,1001)
total = 0
for n in numbers:
	tests = range(2,n-1)
	prime = True
	for t in tests:
		if n % t == 0:
			prime = False
	if prime:
		total = total + n
		
print total
		
