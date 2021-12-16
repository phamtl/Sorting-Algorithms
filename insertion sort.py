def insertion_sort(arr):
	for j in range(1, len(arr)):
		key = arr[j]
		i = j-1
		while i >=0 and key < arr[i]:
			arr[i + 1] = arr[i]
			i -= 1
		arr[i+1] = key

import timeit
import random
arr = []
#print("Initial array:")
for i in range(0,1000):
        a = random.randint(0,1000)
        arr.append(a)
def sort():
        insertion_sort(arr)
print(timeit.timeit(sort, number=1))
#print ("Sorted array is:")
#for i in range(len(arr)):
#	print(arr[i])
