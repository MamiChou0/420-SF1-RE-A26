phrase = input('Phrase : ').replace(' ', '').lower()
phrase_inverse = phrase[::-1]
if phrase_inverse == phrase:
    print('Palindrome magique !')
else:
    print('Pas un palindrome')
