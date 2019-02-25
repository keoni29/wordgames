''' Describe a word by taking two trigrams from it and selecting two random words with the same trigram in it to describe it.
'''
import sys
import random

# Default dictionary location
filename = '/usr/share/hunspell/en_US.dic'

# Commandline parameters
argc = len(sys.argv)

if argc >= 2:
	word = sys.argv[1]
else:
  sys.exit("Usage: {0} word".format(sys.argv[0]))

#digram = [''.join((b,c)) for (b,c) in zip(word[1:-1],word[2:-1])]
trigram = [''.join((b,c,d)) for (b,c,d) in zip(word[1:-1],word[2:-1],word[3:-1])]
matches = trigram
random.shuffle(matches)

print(matches)
 
# Read the dictionary
try:
	with open(filename,'r') as dic_file:
		lines = dic_file.readlines()
except IOError:
	print("Error: Dictionary file does not exist.")
	pass
foo = set(line.strip().split('/')[0].lower() for line in lines)
try:
    foo.remove(word)
except:
    pass

for match in matches:
    result1 = set(filter(lambda x: ('ing' in x[-3:]) and (match in x[1:-1]),foo))
    foo2 = set(filter(lambda x: 'ing' not in x[-3:],foo))
    result2 = set(filter(lambda x: match in x[1:-1],foo2))
    
    if result1 and result2:
        for _ in range(5):
            print(word + ': ' + '_'.join((random.choice(tuple(result1)), random.choice(tuple(result2)))))
        break
