word = input("Speak, human")
word = word.lower()
output = ""

if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
	output += word + "yay"
else:
	output += word[1,1000] + word[0] + "ay"	
print output