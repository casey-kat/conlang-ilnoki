from collections import Counter
import numpy as numpy
import random


consonants = ['m','my','n','ny','y','p','b','k','ky','g','t','ts','d','s','z','f','v','w','l']
vowels = ['i','u','e','o','a']
finals = ['l','n']

illegal_syllables = ['', 'myi', 'nyi', 'kyi', 'yi', 'wu']
illegal_l_consonants = ['', 'h', 'l']
illegal_n_consonants = ['', 'h','m','my','n','ny','ky','li']

legal_l_consonants = [i for i in consonants if i not in illegal_l_consonants]
legal_n_consonants = [i for i in consonants if i not in illegal_n_consonants]

# phoneme_counter = Counter()

word_count = 1296
def gen_word():
	syllable_array = []
	syllable_count = int(round(numpy.random.normal(5,5)) / 5) + 2
	for i in range(syllable_count):
		syllable = ['','','']

		is_illegal = True
		while is_illegal == True:
			if i == 0 and random.randrange(0,4) >= 0:
				syllable[0] = random.choice(consonants)
			elif i > 0:
				if syllable_array[i-1][2] == 'l':
					syllable[0] = random.choice(legal_l_consonants)
				elif syllable_array[i-1][2] == 'n':
					syllable[0] = random.choice(legal_n_consonants)
				else:
					syllable[0] = random.choice(consonants)
			syllable[1] = random.choice(vowels)

			is_illegal = False
			test_syllable = ''
			for letter in syllable:
				test_syllable += letter
			for illegal_syllable in illegal_syllables:
				if test_syllable == illegal_syllable:
					is_illegal = True



		if random.randrange(0,4) == 0:
			syllable[2] = random.choice(finals)

		# phoneme_counter[syllable[0]] += 1
		# phoneme_counter[syllable[1]] += 1
		# phoneme_counter[syllable[2]] += 1

		syllable_array.append(syllable)
	
	word = ''
	for syllable in syllable_array:
		for letter in syllable:
			word += letter
	if word == '':
		word = gen_word()
	
	word = word.replace('nb', 'mb')
	word = word.replace('np', 'mp')

	return word

sentence = ''
for _ in range(word_count):
	sentence += gen_word() + ' '

# for i in range(len(phoneme_counter)):
# 	entry = phoneme_counter.most_common()[i]
# 	letter = entry[0]
# 	count = entry[1]
# 	if (letter in consonants or letter in vowels) and count > 0:
# 		print('{}: {}'.format(letter, count))


print(sentence)
