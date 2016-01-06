# python learning exercises

# Functions

def echo(thing):
	return thing

def swap(thing1, thing2):
	return thing2, thing1

	
def main_function():
	print "testing echo('marco'): ", echo('marco')
	print "testing echo('shut up'): ", echo('no, you shut up')
	print "testing swap('fame', 'fortune')", swap('fame', 'fortune')


#Arithmetic Functions

def reverse(x):
	return -x

def plus(a, b):
	return a + b
	
def diff(x, y):
	return x - y
	
def abs_diff(d, b):
	diff = b - d
	if diff < 0:
		diff *= -1
	return diff
	
def divide(q, w):
	return q / w
	
def remainder(g, h):
	return g % h

def power(x, e):
	answer = 1
	for i in range(e):
		answer *= x
	return answer

def power2(x, e):
	return x ** e
	
def calculate(a, b, c, d, e,):
	return (a + b / d - e) * c
	
def ratio(al , fred):
	if al > fred:
		return al / fred
	else:
		return fred / al
		
def pythagoras(a, b):
	return (a**2 + b**2)**(.5)

def main_arithmetic():
	print "test reverse(3): ", reverse(3)
	print "test reverse(-3): ", reverse(-3)
	print "testing plus(1, 1): ", plus(1, 1)
	print "testin' diff(12, 5): ", diff(12, 5)
	print "test abs_diff(10, 5): ", abs_diff(10, 5)
	print "test divide(10, 2): ", divide(10, 2)
	print "test remainder(133, 19): ", remainder(133, 19)
	print "test power(2, 3): ", power(2, 3)
	print "test power2(2, 3): ", power2(2, 3)
	print "test calculate(1, 2, 3, 4, 5): ", calculate(1, 2, 3, 4, 5)
	print "test ratio(3.2, 7.8): ", ratio(3.2, 7.8)
	print "test ratio(7.8, 3.2): ", ratio(7.8, 3.2)
	print "testing pythagoras(3, 4): ", pythagoras(3, 4)
	print "testing pythagoran(35, 67): ", pythagoras(35, 67)
	
	
	
#Boolean Expressions (logic)

def reverse(zack):
	return not zack
	
def band(a, b):
	if a == True and b == True:
		return True
	else:
		return False
	
def band2(a, b):
	return a and b
	
def bor(a, b):
	if a == True or b == True:
		return True
	else:
		return False
	
def bor2(a, b):
	return a or b
	
def xsame(b, g):
	return b == g
	
def xor(b, g):
	return b != g
		
def main_boolean():
	print "test reverse(True): ", reverse(True)
	print "test reverse(False): ", reverse(False)
	print "test reverse(1): ", reverse(1)
	print "test reverse(0): ", reverse(0)
	print "test reverse(18): ", reverse(18)	
	print "test band(True, True): ", band(True, True)
	print "test band2(False, True): ", band2(False, True)
	print "test bor(True, False): ", bor(True, False)
	print "test bor(False, False): ", bor2(False, False)
	print "test xsame(True, True): ", xsame(True, True)
	print "test xsame(False, True): ", xsame(False, True)
	print "test xsame(False, False): ", xsame(False, False)
	print "test xsame(True, False): ", xsame(True, False)
	print "test xor(True, False): ", xor(True, False)
	print "test xor(False, True): ", xor(False, True)
	print "test xor(True, True): ", xor(True, True)
	print "test xor(False, False): ", xor(False, False)
	

#Boolean Expressions (numbers)

def positive(n):
	if n > 0:
		return True
	else:
		return False
		
def bigger(r, p):
	if r > p:
		return True
	else:
		return False

def no_diff(a, b):
	if a == b:
		return True
	else:
		return False
		
def not_same(a, b):
	if a != b:
		return True
	else: 
		return False
		
def less_than(a, b):
	return a < b
	
def at_least_13(n):
	return n >= 13
	
def at_most_13(n):
	return n <= 13
		
		
		
def main_booleannumbers():
	print "test positive(29): ", positive(29)
	print "test positive(-29): ", positive(-29)
	print "test bigger(200, 10): ", bigger(200, 10)
	print "test bigger(10, 200): ", bigger(10, 200)
	print "test no_diff(100, 100): ", no_diff(100, 100)
	print "test no_diff(10, 100): ", no_diff(10, 100)
	print "test not_same(100, 100): ", not_same(100, 100)
	print "test not_same(10, 100): ", not_same(10, 100)
	print "test less_than(30, 50): ", less_than(30, 50)
	print "test less_than(50, 30): ", less_than(50, 30)	
	print "test at_least_13(12): ", at_least_13(12)
	print "test at_least_13(14): ", at_least_13(14)
	print "test at_most_13(14): ", at_most_13(14)
	print "test at_most_13(12): ", at_most_13(12)
	print "test at_most_13(13): ", at_most_13(13)
	
	
#conditionals


def biggest(x, y):
	if x > y:
		return x
	else: 
		return y	#Don't need else!
		
def smallest(ab, yb):
	if ab < yb:
		return ab
	else:
		return yb
		
def letter_grade(score):
	if score >= 90:
		return "A"
	elif score >= 80:
		return "B"
	elif score >= 70:
		return "C"
	elif score >= 60:
		return "D"
	else: 
		return "F"
		
def food_tax(subtotal, grocery):
	if grocery:
		return subtotal * .03
	else:
		return subtotal * .0725
		
def same(a, b, c):
	if a == b and a == c:
		return True
	else: 
		return False

def big3(a, b, c):
	if a > b and a > c:
		return a
	elif b > a and b > c:
		return b
	else:
		return c
		
def small_sum(a, b, c):
	if a < b and b < c:
		return a + b
	elif c < b and a < b:
		return a + b
	elif b < c and c < a:
		return b + c
		
def meat_loaf(a, b, c):
	if a == b and a != c:
		return True
	elif b != a and b == c:
		return True
	elif a != b and a == c:
		return True
	else:
		return False
		
def big3reorder(a, b, c):
	if a == big3(a, b, c):
		return a, biggest(b, c), smallest(b, c)
	elif b == big3(a, b, c):
		return b, biggest(a, c), smallest(a, c)
	else:
		return c, biggest(a, b), smallest(a, b)
		
		
def positive_multiple(x, y):
	product = x * y
	if not positive(product):
		return product * -1
	else:
		return product

	
	
def main_conditional():
 	print "test biggest(13, 14): ", biggest(13, 14)
 	print "test biggest(15, 12): ", biggest(15, 12)
	print "test smallest(50, 12): ", smallest(50, 12)
	print "test letter_grade(73): ", letter_grade(73)
	print "testing food_tax(12.45, True): ", food_tax(12.45, True)
	print "testing food_tax(12.45, False): ", food_tax(12.45, False)
	print "test same(1, 2, 3): ", same(1, 2, 3)
	print "test same(1, 1, 1): ", same(1, 1, 1)
	print "test big3(1, 2, 3): ", big3(1, 2, 3)
	print "test big3(1, 5, 2): ", big3(1, 5, 2)
	print "test big3(5, 2, 3): ", big3(5, 2, 3)
	print "test small_sum(5, 6, 7): ", small_sum(5, 6, 7)
	print "test small_sum(1, 2, 3): ", small_sum(1, 2, 3)
	print "test meat_loaf(1, 3, 1): ", meat_loaf(1, 3, 1)
	print "test meat_loaf(5, 5, 1): ", meat_loaf(5, 5, 1)
	print "test meat_loaf(4, 4, 4): ", meat_loaf(4, 4, 4)
	print "test big3reorder(5, 8, 2): ", big3reorder(5, 8, 2)
	print "test positive_multiple(50, 2): ", positive_multiple(50, 2)
	print "test positive_multiple(50, -2): ", positive_multiple(50, -2)
	print "test positive_multiple(-50, -2): ", positive_multiple(-50, -2)
	
	
	#counted loops
	
def total(x):
	t = 0
	for num in range(x):
		t += num
	return t
	
def total_slice(a, b):
	t = 0
	for num in range(a, b):
		t += num
	return t

def total_slice2(a, b):
	t = 0
	for num in range(smallest(a, b), biggest(a, b)):
		t += num
	return t
	
def total_odds(a, b):
	t = 0 
	for num in range(a, b):
		if num % 2 == 1:
			t += num
	return t

def total_evens(a, b):
	t = 0 
	for num in range(a, b):
		if num % 2 == 0:
			t += num
	return t
	
def total_7s(a, b):
	t = 0 
	for num in range(a, b):
		if num % 7 == 0:
			t += num
	return t
	
def total_non7s(a, b):
	t = 0 
	for num in range(a, b):
		if num % 7 != 0:
			t += num
	return t
	
def squares(x):
	ts = 0
	for num in range(x):
		ts += num **2 
	return ts
	
	
	
def main_counted_loops():
	print "testing total(5): ", total(5)
	print "testing total(63): ", total(63)
	print "testing total_slice(3, 8): ", total_slice(3, 8)
	print "testing total_slice2(8, 3): ", total_slice2(8, 3)
	print "testing total_slice2(3, 8): ", total_slice2(3, 8)
	print "test total_odds(2, 10): ", total_odds(2, 10)
	print "test total_evens(2, 10): ", total_evens(2, 10)
	print "test total_7s(2, 30): ", total_7s(2, 30)
	print "test total_non7s(2, 10): ", total_non7s(2, 10)
	print "test squares(5): ", squares(5)
	print "test squares(500): ", squares(500)
	
	
#strings

def hello():
	return "hello"
	
def nothing():
	return "" 
	
def second_letter(two):
	return two[1]
	
def one_letter(str, num):
	return str[num]
	
def concatenate(silvester, tony):
	return silvester + tony
	
def beauty(yes):
	return yes + 'beauty'
	
def slice_of_life(str):
	return str[2: 5]
	
def slice_of_heaven(str, num):
	return str[num + 4]
	
def slice_of_perfection(str, a, b):
	return str[a: b]
	
def length(str):
	return len(str)
	


	
def main_string():
	print "test hello(): ", hello()
	print "test nothing(): ", nothing()
	print "test second_letter('cheese'): ", second_letter('cheese')
	print "test one_letter('random', 5): ", one_letter('random', 5)
	print "test concatenate('yes ', 'no'): ", concatenate('yes ', 'no')
	print "test beauty('yes '): ", beauty('yes ')
	print "test slice_of_life('bread'): ", slice_of_life('bread')
	print "test slice_of_heaven('heaven', 1): ", slice_of_heaven('heaven', 1)
	print "test slice_of_perfection('perfection', 2, 7): ", slice_of_perfection('perfection', 2, 7)
	print "test length('test'): ", length('test')
	print "test length('perfection'): ", length('perfection')
	
	
#lists

def short_list():
	return [1, 2, 3]
	
def hollow():
	return[]
	
def third_value(a):
	return a[2]
	
def one_value(l, n):
	return l[n]
	
def add_list(a, b):
	return a + b
	
def pie(list):
	return list + [314]
	
def grow_one(a, b):
	a.append(b)
	return a
	
def sub_list(z):
	return z[1: 5]
	
def sub_list2(list, num):
	return list[num: num+3]
	
def sub_list3(list, a, b):
	return list[a: a+b]
	
def list_length(l):
	return len(l)
	

def main_list():
	print "test short_list(): ", short_list()
	print "test hollow(): ", hollow()
	print "test thrid_value(['person', 'place', 'thing']): ", third_value(['person', 'place', 'thing'])
	print "test one_value(['1', '2', '3'], 2): ", one_value(['1', '2', '3'], 2)
	print "test add_list(['first', 'second'], [1, 2]): ", add_list(['first', 'second'], [1, 2])
	print "test pie(['pie is']): ", pie(['pie is'])
	print "test grow_one(['yes']): ", grow_one(['yes'], 'no')
	print "test sub_list(['even', 'more', 'bloody', ' things',]): ", sub_list(['even', 'more', 'bloody', ' things',])
	print "test sub_list2(['yes', 'no', 'maybe', 'things'], 3): ", sub_list2(['yes', 'no', 'maybe', 'things'], 3)
	print "test sub_list2(['yes', 'no', 'maybe', 'things'], 1, 3): ", sub_list3(['yes', 'no', 'maybe', 'things'], 1, 3)
	print "test list_length(['yes', 'no', 'maybe', 'things', 'person', 'place', 'thing']): ", list_length(['yes', 'no', 'maybe', 'things', 'person', 'place', 'thing'])
	
	
#sequence loops

def list_total(numbers):
	total = 0
	for number in numbers:
		total += number
	return total
	
def list_total2(numbers):
	total = 0
	for number in numbers:
		if number % 2 == 0:
			total += number
	return total
	
def list_total3(numbers):
	total = 0
	for i in range(1, len(numbers), 2):
		total += numbers[i]
	return total
		
def is_lowercase(letter):
	alpha = 'abcdefghijlkmnopqrstuvwxyz'
	return letter in alpha		
		
		
		
def string_lower_count(str):
	count = 0
	for c in str:
		if is_lowercase(c):
			count += 1
	return count
	
def digit(char):
	digit = '123456789'
	return char in digit
	
def string_digit_count(str):
	count = 0
	for c in str:
		if digit(c):
			count += 1
	return count	
	
def string_word_count(s):
	count = 0
		for i in range(len(s)):
			if s[i] == ' ' and is_letter(s[i+1]):
		

		
def main_sequence_loop():
	class_iqs = [150, 100, 2, 300000, 130, 98, 6, 28, 6, 5, 87, 51]
	lucky_numbers = [13, 7, 21, 12, 5, 777, 42, 88, 11, 33, 22, 222, 15]
	print "test list_total(class_iqs): ", list_total(class_iqs)
	print "test list_total2(lucky_numbers): ", list_total2(lucky_numbers)
	print "test list_total3(lucky_numbers): ", list_total3(lucky_numbers)
	print "test string_lower_count('Alvey is handsome'): ", string_lower_count(' Alvey is handsome')
	print "test string_digit_count(
	
	
def main():
		main_function()
		main_arithmetic()
		main_boolean()
		main_booleannumbers()
		main_conditional()
		main_counted_loops()
		main_string()
		main_list()
		main_sequence_loop()
		
main()