# author: joshsanyal

thingstodo = ["watch a Rockets game", "visit the southern hemisphere", "go camping"]

for thing in thingstodo:
	answer = input ( "Would you want to " + thing + "?" )
	if answer == "yes":
		print "Then do " + thing
	if answer == "no":
		print "Then don't " + thing