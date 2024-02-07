'''
def partition_naive(stuff):
	pivot = stuff[0]
	low = []
	high = []
	for i in range(len(stuff)):
		if stuff[i] <= pivot:
			low.append(stuff[i])
		elif stuff[i] > pivot:
			high.append(stuff[i])
	stuff.clear()
	stuff.append(low)
	stuff.append(pivot)
	stuff.append(high)

	return stuff.index(pivot)


stuff = [7,3,9,5,1,0]
print(partition_naive(stuff))
'''

def partiiton_in_place(stuff):
	pivot = stuff[0]
	L = stuff[0]
	U = stuff[-1]
	done = False
	while not done:
		while L < pivot:
			L += 1
		while U >= pivot:
			U -= 1
		if L >= U:
			done = True
		else:
			stuff[L], stuff[U] = stuff[U], stuff[L]
		pivot, stuff[U] = stuff[U], pivot

stuff = [10, 5, 16, 14, 2, 10, 13]
print(partiiton_in_place(stuff))



def random_list(size):
	list = []
	n = 1
	while len(list) <= len(range(size)):
		for i in range(size):
			list.append(n)
			n += 1
		return list


size = 20
print(random_list(size))




























