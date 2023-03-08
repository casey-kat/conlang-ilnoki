from collections import Counter
import numpy
import random

consonants = ['m', 'n', 'p', 'b', 'y', 'k', 'ky', 'g', 't', 'ts', 'd', 's', 'sw', 'z', 'f', 'v', 'w', 'l']
vowels = ['i', 'u', 'e', 'o', 'a']  # ɪ ə
finals = ['l', 'n']

illegal_syllables = ['', 'kyi'] # illegal_syllables = ['', 'kyi', 'yi', 'wu']

illegal_l_consonants = ['l']
illegal_n_consonants = ['m', 'n']
legal_l_consonants = [i for i in consonants if i not in illegal_l_consonants]
legal_n_consonants = [i for i in consonants if i not in illegal_n_consonants]

def gen_word(syllable_count=int(round(numpy.random.normal(5, 5)) / 5) + 2):
    syllable_array = []
    for i in range(syllable_count):
        syllable = ['', '', '']

        # vowel
        syllable[1] = random.choice(vowels)

        # consonant
        while True:
            if random.randrange(0, 4) >= 0:
                syllable[0] = random.choice(consonants)
            if i > 0:
                syllable[0] = random.choice(consonants)
                if syllable_array[i-1][2] == 'l':
                    syllable[0] = random.choice(legal_l_consonants)
                elif syllable_array[i-1][2] == 'n':
                    syllable[0] = random.choice(legal_n_consonants)
            test_syllable = '{}{}'.format(syllable[0], syllable[1])
            if test_syllable not in illegal_syllables:
                break

        # final
        if random.randrange(0, 4) == 0:
            syllable[2] = random.choice(finals)
        
        # add to word
        syllable_array.append(syllable)

    word = ''
    for syllable in syllable_array:
        for letter in syllable:
            word += letter

    # romanized allophony
    word = word.replace('nb', 'mb')
    word = word.replace('np', 'mp')
    word = word.replace('ny', 'ŋy')
    word = word.replace('nk', 'ŋk')
    word = word.replace('nky', 'ŋky')
    word = word.replace('ng', 'ŋg')

    return word