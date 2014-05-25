x = 0
y = 1
z = 0

while x < 1000000:
	print x
	z = y
	y = x + y
	x = z