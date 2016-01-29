def show_instructions():
	print '''Pick a number between 1 and 1000 and I will try to guess it.
		I can do this in no more than 10 guesses'''
	print '''After each guess, enter:
		0 - if I got it right
		-1 - if I guessed too high
		1 - if I guessed too low.''' 
def take_guess():
	high = 1000
	low = 0
	guess = high + low / 2
	keep_asking = 1
	while keep_asking == 1:
		print guess
	response == raw_input('enter 1, -1, 0')
	if response == 0:
		print "I'm right"
		keep_asking == 0
	elif response == 1:
		print "I'm too high"
		keep_asking == 1
		high = high / 2
		low = 0
		print guess
	elif response == -1:
		print "I'm too low"
		keep_asking == 1
		high = high
		low = high + low / 2
		print guess
def main():
	show_instructions()
	take_guess()
