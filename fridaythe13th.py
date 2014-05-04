# author: joshsanyal
years = range(1900,2015)
months = range(1,13)
total = 0

for year in years:
	for month in months:
		days = range(1,32)
		if month == 2:
			days = range(1,29)
			if year % 4 == 0:
				days = range(1,30)
			if year % 100 == 0:
				days = range(1,29)
			if year % 400 == 0:
				days = range(1,30)
					
		if month == 4 or month == 6 or month == 9 or month == 11:
			days = range(1,31)
			
		for day in days:
			total = total + 1
	
print total