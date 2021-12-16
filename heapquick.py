import math
class HeapQuick:
    def __init__(self, arr, start, end):
        self.arr = arr
        self.start = start
        self.size = 0
        self.end = end
        
    #heapsort
    def leftchild(self, node):
        return 2 * node + 1
    def rightchild(self, node):
        return (2 * node) + 2
    def parent(self, node):
        return node // 2

    def max_heapify(self, node):
        l = self.leftchild(node)
        r = self.rightchild(node)
        if l <= (self.size-1) and self.arr[l] > self.arr[node]:
            largest = l
        else:
            largest = node
        if r <= (self.size-1) and self.arr[r] > self.arr[largest]:
            largest = r
        if largest != node:
            self.arr[node], self.arr[largest] = self.arr[largest], self.arr[node]
            self.max_heapify(largest)

    def build_max_heap(self):
        self.size = len(arr)
        for i in range((len(self.arr) // 2), -1, -1):
            self.max_heapify(i)

    def heapsort(self):
        self.build_max_heap()
        for i in range((len(self.arr)-1), 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            self.size -= 1
            self.max_heapify(0)

    #quicksort
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
        if len(arr) == 0:
            return "No array"
        if len(arr) == 1:
            return self.arr
        if start < end:
            mid = self.partition(start, end)
            self.quick_sort(start, mid - 1)
            self.quick_sort(mid + 1, end)
            
    def sort(self, start, end):
        depth = 2 * math.floor(math.log2(end - start))
        self.mixsort(start, end, depth)

    def mixsort(self, start, end, depth):
        if end - start <= 1:
            return self.arr
        elif depth == 0:
            self.heapsort()
        else:
            self.quick_sort(start, end)

import random
import timeit
for _ in range(25):
    arr = []
    for i in range(0, 1000):
        a = random.randint(0,1000)
        arr.append(a)
    n = len(arr)
    hq = HeapQuick(arr, 0, n-1)
    def sort():
        hq.sort(0, n-1)
    print(timeit.timeit(sort, number=1))
#print(arr)









            
        
                         
