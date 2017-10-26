''' Digram
	Two successive letters in a word is called a digram. The word FOUR contains
	the digrams FO, OU and UR.

	The game is played as follows: A player shouts a digram. The other players 
	need to write down as many words that contain the digram as possible. The 
	word cannot start or end with the digram or in the middle of a combined
	word. E.g. for digram SA, applesauce is disqualified.

	The computer is really good at this game if you provide it with a long 
	dictionary file. Any text or .dic file will work. By default the hunspell 
	dictionary is used, since it is already installed on most systems.

	Known issues:
	- If the dictionary file contains combined words they will be matched.
	- User input is not checked. Numbers and symbols are allowed. Any string
		length is allowed.
'''
import sys

# Some example digrams
digram = [
	'az', 'cc', 'ff', 'gg', 'gh', 'kp', 'kr', 'lm', 'mn', 'nj', 'pg', 'sr',
	'tv', 'wv', 'sa']

# Default dictionary location
filename = '/usr/share/hunspell/en_US.dic'

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

# Show the result
for d,answer in result.iteritems():
	print 'Answers for digram "'  + d + '" are:'
	print answer
