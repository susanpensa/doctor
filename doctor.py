"""
Program: doctor.py
Author: Susan 11/3/2021

Conducts an interactive session of nondirective psychotherapy.
"""

import random

# Global variables (data pool)
hedges = ("Please tell me more.", "Many of my other patients tell me the same thing.", "Please continue.", "Go on, go on...", "You don't say...")

qualifiers = ("Why do you say that ", "You seem to think that ", "Can you explain why ", "Think about and describe why ", "Tell me how ")

replacements = {"I":"you", "me":"you", "my":"your", "we":"you", "us":"you", "mine":"yours", "you":"I", "am":"are"}

# definition of the reply() function
def reply(sentence):
	"""Builds and returns a reply to a sentence."""
	probability = random.randint(1, 4)
	if probability == 1:
		return random.choice(hedges)
	else:
		return random.choice(qualifiers) + changePerson(sentence)
		
# definition of thge changePerson() function
def changePerson(sentence):
	"""Replaces first-person pronouns with second-person pronouns."""
	# take the user input sentence data and split it with the array
	words = sentence.split()
	# empty array to hold onto the modified words
	replyWords = []
	# loop through the words array and decide if the word the loop os examining needs to be replaced
	for word in words:
		replyWords.append(replacements.get(word, word))
	# now that the replyWords array is complete let's turn it back into a string so it can be returned
	return " ".join(replyWords)

# definition of the main() function
def main():
	"""Handles interacton between patient and doctor."""
	print("Good morning, I hope you are well today.")
	print("What can I do for you?")
	# keep this app running until the user quits
	while True:
		sentence = input("Type a response or QUIT to exit >>")
		# check if the user typed QUIT, if so we can exit the program.
		if sentence.upper() == "QUIT":
			print("Have a nice day!")
			break;
		# if we are here, the user must not have typed QUIT
		print(reply(sentence))

# call to the main() function for program execution
if __name__ == "__main__":
	main()