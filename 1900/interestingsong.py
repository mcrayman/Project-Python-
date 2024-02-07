drink = input('What are we drinking today? ')
bottles = int(input('And how many bottles are we starting with? '))

while bottles > 1:
	print(bottles, 'bottles of', drink,'on the wall,')
	print(bottles, 'bottles of', drink,'\b.')
	print('Take one down, pass it around,')
	bottles -= 1
	if bottles == 1:
		print(bottles, 'bottle of', drink,'on the wall.')
	else:
		print(bottles, 'bottles of', drink,'on the wall.')
	print('')
	

bottles = 1
print(bottles, 'bottle of', drink,'on the wall,')
print(bottles, 'bottle of', drink,'\b.')
print('Take one down, pass it around,')
bottles -= 1
print('No more bottles of', drink,'on the wall.')
