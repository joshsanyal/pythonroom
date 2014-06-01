words = input("Insert word for translation to pig latin")
words = words.lower()
words = words.split(" ")
vowels = ["a", "e", "i", "o", "u"]
output = ""
for word in words:
	if word[0] in vowels:
		output += word + "yay "
	else:
		start = 0
		for letter in list(word):
			if letter in vowels:
				break
			else:
				if letter is "y":
					break
				else:
					start += 1
		output += word[start:] + word[:start] + "ay "

print output