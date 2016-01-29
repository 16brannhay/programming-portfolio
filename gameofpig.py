#Game of pig.
import random
def roll_die(sides):
	r = random.randrange(1, sides+1)
	return r

def take_turn(player):
	point = 0
	keep_rolling = 1
	print "It's your turn player" , player
	raw_input("press enter to begin")
	while keep_rolling == 1:
		r = roll_die(6)
		print "you got a" , r
		if r == 1:
			point = 0
			keep_rolling = 0
			r = take_turn(2)
		else:
			point += r
			print "your point total is" , point
			y = raw_input ("do you want to continue? y= yes n= no")
			if y == "y":
				keep_rolling = 1
			else:
				keep_rolling = 0
				print "your turn is over"
				return point
				
def show_instructions():
	print ''' Welcome to the game of Pig. To win, be the player with the most points at the
	end of the game. The game ends at the end of a round where at least one player has 100
	or more points. On each turn, you may roll the die as many times as you like to 
	obtain more points. However, if you roll a 1, your turn is over, and you do not obtain
	any points that turn.'''
	
def main():
	show_instructions()
	p1 = 0
	p2 = 0
	while p1 < 100 and p2 < 100:
		print "player 1 points are: " +str(p1)
		print "player 2 points are: " +str(p2)
		r = take_turn(1)
		p1 += r
		print "player points are: " +str(p1)
		print "player points are: " +str(p2)
		r = take_turn(2)
		p2 += r
		print "the game is over"
		if p1>p2:
			print "player one wins"
		elif p1<p2:
			print "player two wins"
		else:
			print "tie game"

main()
take_turn(1)
take_turn(2)


