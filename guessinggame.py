#High low guessing game.
def show_instructions():
	print '''pick a number between 1 and 1000 and I will try to guess it.
	I can do this in no more then 10 guesses.
	After each guess, enter: 
	0 - if I got it right 
	-1 - if I guessed too high
	1 - if I guessed too low.'''
def take_guess():
	low = 1
	high = 1000
	