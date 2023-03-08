from collections import Counter
import json

counter = Counter()

def calculate():
	dictionary = {}
	with open("dictionary.json", "r") as file:
		dictionary = json.load(file)

	meanings = {}
	for key, value in dictionary.items():
		if value not in meanings:
			meanings[value] = []
		meanings[value].append(key)

	for key, value in dictionary.items():
		counter[value] += 1

	counter_output = ''
	for i in range(len(counter)):
		entry = counter.most_common()[i]
		word = entry[0]
		count = entry[1]
		if count > 0:
			counter_output += '{}: {} ---- {}\n'.format(word, count, meanings[word])
		print(i)
		if i >= 99:
			break

	with open('word_frequencies.txt', 'w') as f:
		print(counter_output, file=f)
