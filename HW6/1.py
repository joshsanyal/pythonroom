### Check if an inputted word is a palindrome

word = input("Speak, human.")
StartOfWord = 0
endOfWord = len(word) -1
for i in range(endOfWord):
	# Check if the word reads the same going forward and backward
	start = 0
	if word[start] = word[Endofword - start]:
		start = start + 1
	else:
		print "Not a palindrome"