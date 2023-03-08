from word_generator import gen_word

# 1296
# 45565
word_count = 1000

sentence_output = ''
for _ in range(word_count):
    sentence_output += '{} '.format(gen_word())
print(sentence_output)