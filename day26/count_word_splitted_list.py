from posixpath import split


sentence = 'Bonjour je suis un connard'

def split_sentence(sentence):
    return [word for word in sentence.split(' ')]

def count_letters(word):
    return len(word)

output = {word:count_letters(word) for word in split_sentence(sentence)}

print(output)