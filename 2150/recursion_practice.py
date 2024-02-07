
def factorial(n):
	if n == 0:
		return 1
	elif n > 0:
		return n * factorial(n-1)

#recursively returns 2 to the ^th power 
def power_two(n):
	if n == 0:
		return 1
	elif n > 0:
		return 2 * power_two(n = 1) 

#returns whether string is palindrome 
def palindrome(s):
	if len(s) <= 1: #base case - any length of 1 or less is a palindrome
		return True
	elif s[0] != s[-1]:	
		return False
	else:
		return palindrome(s[1:-1])

#recursively returns the reverse of a string
def reverse(s):
	if len(s) <= 1:
		return s 
	else:
		  return reverse(s[1:]) + s[0]

#for i in range(7):
#	print(f'power_two({i}) -> {power_two(i)}')

#for i in range(7):
#	print(f'factorial({i})! = {factorial(i)}')

tests = ['','a','aa','dog','mom','racecar','mother']
for t in tests:
	print(f'palindrome({t}) -> {palindrome(t)}')
	print(f'reverse(\'{t}\') -> \'{reverse(t)}\'')

'''
def fibo(n):
	if n == 0 or n == 1:
		return n 
	elif n > 1:
		return fibo(n - 1) + fibo(n - 2)

def solve_hanoi(n, start, end, mid):
	if n > 0:
		solve_hanoi(n - 1, start, mid, end)
		print(f'Move the disc from {start} to {end}.')
		solve_hanoi(n - 1, mid, end, start)

for i in range(100):
	print(f'fibo({i})! = {fibo(i)}')


solve_hanoi(3, 'A', 'C', 'B')
'''