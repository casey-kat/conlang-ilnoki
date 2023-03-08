

# with open('translations.txt', 'w', encoding='utf-8') as output_file:
#     conwords_file = open('words.txt', 'r', encoding='utf-16LE')
#     conlines = [line for line in conwords_file]

#     engwords_file = open('english_words.txt', 'r', encoding='utf-8')
#     englines = [line for line in engwords_file]

#     output = ''
#     for i in range(min(len(conlines), len(englines))):
#         output += ' {} '.format(englines[i].strip())
#         output += '\n'
#         output += ' {} '.format(conlines[i].strip())
#         output += '\n\n'
#     print(output, file=output_file)

#     conwords_file.close()
#     engwords_file.close()
#     output_file.close()

from word_generator import gen_word
import word_frequency_calculator
import translation_generator
import syllables
import json

dictionary = {}
engwords_file = open('english_words.txt', 'r', encoding='utf-8')
englines = [line for line in engwords_file]
for i in range(len(englines)):
    english_word = englines[i].strip()
    dictionary[english_word] = gen_word(syllables.estimate(english_word))
    if (i % 10000 == 0):
        print(i)
with open('dictionary.json', 'w') as file:
    json.dump(dictionary, file, indent=4)

word_frequency_calculator.calculate()
translation_generator.print_passage()

# with open('translations.txt', 'w', encoding='utf-8') as output_file:
#     engwords_file = open('english_words.txt', 'r', encoding='utf-8')
#     englines = [line for line in engwords_file]

#     output = ''
#     for i in range(len(englines)):
#         english_word = englines[i].strip()
#         output += ' {} '.format(english_word)
#         output += '\n'
#         output += ' {} '.format(gen_word(syllables.estimate(english_word)).strip())
#         output += '\n'
#     print(output, file=output_file)

#     engwords_file.close()
#     output_file.close()
