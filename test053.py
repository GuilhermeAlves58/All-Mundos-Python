phrase = str(input('Type a phrase: ')).strip().upper()
word = phrase.split()
wordtogether = ''.join(word)
reverse = ''
for letter in range(len(wordtogether)-1,-1,-1):
    reverse += wordtogether[letter]
if (wordtogether) == (reverse):
    print(f'{wordtogether} È palidromo e o inverso {reverse}')
else:
    print(f'{wordtogether} Não é palidromo e o inverso {reverse}')