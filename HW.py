# author: joshsanyal
import random
total = 1

people = int(input("How many people are there?"))
flies= int(input("How many flies are in the room?"))

if random.randint(1,1000) < flies:
	print "Someone is blinking."
else:
	print "Nobody is blinking."
if random.randint(1,1000) < flies:
	total = total + 1
print total