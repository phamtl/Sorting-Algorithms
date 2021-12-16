class heap_sort:
    def __init__(self, arr):
        self.size = 0
        self.arr = arr

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

    def print(self):
        for i in range(self.size):
            print(self.arr[i]) 
        print("Size:",self.size)

    def heapsort(self):
        self.build_max_heap()
        for i in range((len(self.arr)-1), 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            self.size -= 1
            self.max_heapify(0)


import random
import timeit
arr = []
for i in range(0,1000):
    n = random.randint(0,1000)
    arr.append(n)
hs = heap_sort(arr)
def sort():
    hs.heapsort()
print(timeit.timeit(sort, number=1))







        
