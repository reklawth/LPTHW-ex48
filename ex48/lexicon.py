'''
This purpose of this program is to provide a scanner, that outputs a tuple to user defined
input.  The tuple is created by matching defined lists of words with similar characteristics
against the user input.

This program should utilize Tuples and works with Python 2.7
'''

# Lexicon: Defined vocabulary of words to be used for this package
direction_words = ['north','south','east','west','down','up','left','right''back']
verbs = ['go','stop','kill','eat']
stop_words = ['the','in','of','from','at','it']
nouns = ['door','bear','princess','cabinet']

def scan(sentence):
	words = sentence.split()
	print('in scan method ' + str(words))

def directions(val):
	sentence = val
	scan(val)
	
	
def verbs(val):
	words = val.split()
	
def stops(val):
	words = val.split()
	
def nouns(val):
	words = val.split()

def numbers(val):
	words = val.split()
	
def errors(val):
	words = val.split()
	

print("Please provide a sentence:")
sentence_line = raw_input('> ')
scan(sentence_line)
print("past")
