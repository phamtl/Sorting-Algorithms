class quicksort:
    def __init__(self, arr, start, end):
        self.arr = arr
        self.start = start
        self.end = end

    def partition(self, start, end):
        x = self.arr[end]
        i = start - 1
        for j in range(start, end):
            if self.arr[j] <= x:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.arr[i+1], self.arr[end] = self.arr[end], self.arr[i+1]
        return i + 1

    def quick_sort(self, start, end):
        if len(self.arr) == 0:
            return "No array"
        if len(self.arr) == 1:
            return self.arr
        if start < end:
            mid = self.partition(start, end)
            self.quick_sort(start, mid - 1)
            self.quick_sort(mid + 1, end)


import random
import timeit
for _ in range(25):
    arr = []
    for i in range(0, 10):
        a = random.randint(0,1000)
        arr.append(a)
    n = len(arr)
    qs = quicksort(arr, 0, n-1)
    def sort():
        qs.quick_sort(0, n-1)
    sort()
    print(timeit.timeit(sort, number=1))
#print(arr)
