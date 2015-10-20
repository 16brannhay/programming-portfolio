#Python learning exercises.

#Functions

def echo(thing):
	return thing
	
def swap(a , b):
	return b , a

def main_function():
	print "testing echo('marco'): ", echo('marco')
	print "testing swap('fame' , 'fortune'): ", swap('fame', 'fortune')
	
#Arithmetic Expressions.

def reverse(x):
	return -x
	
def plus(a , b):
	return a + b

def diff(x , y):
	return x - y
	
def abs_diff(m , n):
	return m - n

def main_arithmetic():
	print "testing reverse(3): ", reverse(3)
	print "testing plus(1 , 2): ", plus(1 , 2)
	print "testing diff(12, 5): ", diff(12 , 5)





def main():
	main_function()
	main_arithmetic()