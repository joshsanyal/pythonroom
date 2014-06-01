word = input("Insert word for translation to pig latin")
word = word.lower()
vowels = ["a", "e", "i", "o", "u"]
output = ""

if word[0] in vowels:
	output += word + "yay"
else:
	start = 0
	for letter in list(word):
		if letter in vowels:
			break
		else:
			start += 1
	output += word[start:] + word[:start] + "ay"

print output