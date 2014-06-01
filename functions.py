# author: joshsanyal

def sayHello():
	print "Hello there!"
	
def sayHelloTo(name):
	print "Hello " + name + "."
	
def sayGreeting(greeting, name):
	print greeting + "there, " + name
	
def sayGoodbye():
	print "See ya later!"
	
def sayGoodbyeTo(name):
	print "see ya " + name + "."
	
def ageOf(person):
	if person == "akhilesh":
		return 9
	if person == "ravi":
		return 9
	if person == "josh":
		return 10
	if person == "keshav":
		return 28
	if person == "yash":
		return 31
	


sayHello()
sayHelloTo("Keshav")
sayGreeting("Hello ", "Akhilesh")
sayGreeting("Hello ", "Josh")
sayGreeting("Goodye ", "Ravi")
print ageOf("akhilesh") + ageOf("ravi") + ageOf("keshav") + ageOf("yash")
sayGoodbye()
