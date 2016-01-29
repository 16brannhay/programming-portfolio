answer = 'yes'
print "guess a number between 1 and 1000"
while answer == 'yes':
	numoftry = 10
	numtoguess = 500
	limitlow = 1
	limithigh = 1000
	while numoftry != 0:
		try:
			print numtoguess
			print "type 1 if guess is too high"
			print "type 2 if guess is too low"
			print "type 3 if guess is right"
			humananswer = int(input()
			if 1 < humananswer > 3:
				print "enter valid answer"
				numoftry = numoftry + 1
			if humananswer == 1
				limithigh = numtoguess
				