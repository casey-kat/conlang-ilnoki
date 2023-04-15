import json
import nltk

passage = "The amber droplet hung from the branch, reaching fullness and ready to drop. It waited. While many of the other droplets were satisfied to form as big as they could and release, this droplet had other plans. It wanted to be part of history. It wanted to be remembered long after all the other droplets had dissolved into history. So it waited for the perfect specimen to fly by to trap and capture that it hoped would eventually be discovered hundreds of years in the future."
passage_tokens = nltk.word_tokenize(passage.lower())

def print_passage():
	dictionary = {}
	with open("dictionary.json", "r") as file:
		dictionary = json.load(file)
		
	for i in range(len(passage_tokens)):
		word = passage_tokens[i]
		if word in dictionary:
			passage_tokens[i] = "{}".format(dictionary[word])
		else: 
			passage_tokens[i] = "[{}]".format(word)

	translated_passage = ""
	for word in passage_tokens:
		translated_passage += "{} ".format(word)

	print('----------------------------------')
	print(passage)
	print('----------------------------------')
	print(translated_passage)
	print('----------------------------------')