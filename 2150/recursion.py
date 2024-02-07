
def power(b, n):
	if n == 0:
		return 1
	elif n == 1:
		return b
	else:
		if n >= 2:
			return (b * power(b, n - 1))
		else:
			return (b * power(b, n + 1))

x = power(5,-3)
print(x)
x = power(5,0)
print(x)
x = power(5,4)
print(x)

def count_positives(stuff):
	if len(stuff) == 0:
		return 0
	return (1 if stuff[0] > 0 else 0) + count_positives(stuff[1:])

stuff = [1,2,3,4,22,14]
x = count_positives(stuff)
print(x)
stuff = [-1,-2,-3,-4,-22,-14]
x = count_positives(stuff)
print(x)
stuff = [-1,2,-3,4,-22,14]
x = count_positives(stuff)
print(x)
stuff = []
x = count_positives(stuff)
print(x)

def all_even(stuff):
	if len(stuff) == 0:
		return True
	else:
		if stuff[0] % 2 == 0 and all_even(stuff[1:]):
			return True
		else:
			return False
	
stuff = [2,4,6,12]
x = all_even(stuff)
print(x)
stuff = [1,3,5,7]
x = all_even(stuff)
print(x)
stuff = [1,2,3,4,6,12]
x = all_even(stuff)
print(x)
stuff = []
x = all_even(stuff)
print(x)
'''
def binary_search(stuff, target):
	mid = (len(stuff) // 2)
	if stuff[mid] == target:
		return mid
	else:
		if stuff[mid] > target:
			return binary_search(stuff[1:mid], target)
		else:
			return binary_search(stuff[mid:], target)
	return -1

stuff = [1,2,3,4,5,6,7,8]
x = binary_search(stuff, 6)
print(x)

'''














