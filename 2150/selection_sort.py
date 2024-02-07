
#examples of sorting lists

def selection_sort(x):
	for j in range(len(x) - 1):
		min_index = j
		for i in range(j, len(x)):
			if x[i] < x[min_index]:
				min_index = i


		x[j], x[min_index] = x[min_index], x[j]

test = [5,3,1,8,1,2]

print(test)
selection_sort(test)
print(test)