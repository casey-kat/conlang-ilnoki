import numpy
import random

consonants = ['m', 'n', 'p', 'b', 'y', 'k', 'ky', 'kw', 'g', 't', 'ts', 'd', 's', 'st', 'sw', 'z', 'f', 'v', 'sh', 'ch', 'w', 'l'] # ʃ
vowels = ['i', 'u', 'e', 'o', 'a']  # ɪ ə
finals = ['l', 'n'] # ŋ
illegal_syllables = ['', 'kyi', 'yi', 'wu'] # illegal_syllables = ['', 'kyi', 'yi', 'wu']

def gen_word(syllable_count=0):
    if syllable_count < 1:
        syllable_count = round(pow(numpy.random.uniform(0.0,1.0) * 2, 2)) + 2
        syllable_count = 2
    syllable_array = []
    for i in range(syllable_count):
        syllable = ['', '', '']

        # vowel
        syllable[1] = random.choice(vowels)

        # consonant
        test_syllable = ''
        while test_syllable in illegal_syllables:
            if random.randrange(0, 4) > 0 or i > 0:
                syllable[0] = random.choice(consonants)
            test_syllable = '{}{}'.format(syllable[0], syllable[1])

        # final
        if random.randrange(0, 4) == 0:
            syllable[2] = random.choice(finals)

        # add to word
        syllable_array.append(syllable)

    word = ''
    for syllable in syllable_array:
        for letter in syllable:
            word += letter

    # remove doubles
    word = word.replace('nm', 'm')
    word = word.replace('nn', 'n')
    word = word.replace('ll', 'l')

    # romanized allophony
    word = word.replace('nb', 'mb')
    word = word.replace('np', 'mp')
    word = word.replace('ny', 'ŋy')
    word = word.replace('nk', 'ŋk')
    word = word.replace('nky', 'ŋky')
    word = word.replace('ng', 'ŋg')

    return word