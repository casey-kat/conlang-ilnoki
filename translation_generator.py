import json
import nltk

passage = "The man found joy in the daily routine of life. He awoke at the same time, ate the same breakfast and drove the same commute. He worked at a job that never seemed to change and he got home at six' sharp every night. It was who he had been for the last ten years and he had no idea that was all about to change."
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
