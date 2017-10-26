''' Digram
	Two successive letters in a word is called a digram. The word FOUR contains
	the digrams FO, OU and UR.

	The game is played as follows: A player shouts a digram. The other players 
	need to write down as many words that contain the digram as possible. The 
	word cannot start or end with the digram or in the middle of a combined
	word. E.g. for digram SA, applesauce is disqualified.

	To make this game even more challenging the digram cannot be at the start of
	a syllable.

	The computer is really good at this game if you provide it with a long 
	dictionary file. Any text or .dic file will work. By default the hunspell 
	dictionary is used, since it is already installed on most systems.

	Known issues:
	- Some words are not correctly hyphenated.
	- User input is not checked. Numbers and symbols are allowed. Any string
		length is allowed.
'''
import pyphen
import sys

# Some example digrams
digram = [
	'az', 'cc', 'ff', 'gg', 'gh', 'kp', 'kr', 'lm', 'mn', 'nj', 'pg', 'sr',
	'tv', 'wv', 'sa']

# Default dictionary location
filename = '/usr/share/hunspell/en_US.dic'

# Configure pyphen
my_lang = 'en_US'

if not pyphen.language_fallback(my_lang) in pyphen.LANGUAGES:
	sys.exit('Could not find dictionary for hyphenation')
	#TODO continue without checks for digrams at the start of syllables

dic = pyphen.Pyphen(lang=my_lang)

# Commandline parameters
argc = len(sys.argv)

if argc >= 2:
	digram = sys.argv[1:]

# Read the dictionary
try:
	with open(filename,'r') as dic_file:
		lines = dic_file.readlines()
except IOError:
	print "Error: Dictionary file does not exist."
	pass

# Show the player the digrams he just typed in
print 'Playing digram for ' + ' '.join(digram) + '!'

# Play the game
result = {d:set(filter(lambda x: d in x[1:-1],set(line.strip().split('/')[0].lower() for line in lines))) for d in digram}

# Judge and show the results
for d,answer in result.iteritems():
	print 'Answers for digram "'  + d + '" are:'

	for a in answer:
		try:
			if d in [a[p:p+2] for p in dic.positions(a)]:
				print '>' + dic.inserted(a)
			else:
				print dic.inserted(a)
		except UnicodeDecodeError:
			print '>'
			pass