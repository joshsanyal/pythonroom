# author: joshsanyal
import random
pictures = 1

people = int(input("How many people are there?"))
flies= int(input("How many flies are in the room?"))

if random.randint(1,1000) < flies:
	print "Someone is blinking."
		pictures = pictures + 1
else:
	print "Nobody is blinking."
print pictures