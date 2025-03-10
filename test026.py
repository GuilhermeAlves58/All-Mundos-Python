phrase= str(input('Type a phrase ')).strip()
print('The letter A appears {} times'.format( phrase.lower().count('a')))
print('The first time letter A appears is in position {}'.format(phrase.lower().find('a')+1))
print('The last time letter A appears is in position {}'.format(phrase.lower().rfind('a')+1))