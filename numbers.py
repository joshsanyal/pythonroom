# author: joshsanyal

numbers = range(1,101)
total = 0

for number in numbers:
	if number % 3 or number % 5 == 0:
		total = total + number
		
print total