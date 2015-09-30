def palindrome(s):
	return s == s[::-1]
if_name_ == '_main_':
	s = raw_input("Enter a string: ")
	if palindrome(s):
		print "Yay a palindrome"
	else:
		print "Oh no, not a palindrome"