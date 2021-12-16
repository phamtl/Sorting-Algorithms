class maxheap:
    def __init__(self):
        self.size = 0
        self.arr = []

    def leftchild(self, node):
        return 2 * node + 1
    def rightchild(self, node):
        return (2 * node) + 2
    def parent(self, node):
        return node // 2

    def max_heapify(self, node):
        l = self.leftchild(node)
        r = self.rightchild(node)
        if l <= (self.size - 1) and self.arr[l] > self.arr[node]:
            largest = l
        else:
            largest = node
        if r <= (self.size - 1) and self.arr[r] > self.arr[largest]:
            largest = r
        if largest != node:
            self.arr[node], self.arr[largest] = self.arr[largest], self.arr[node]
            self.max_heapify(largest)

    def build_max_heap(self):
        for i in range((len(self.arr) // 2), -1, -1):
            self.max_heapify(i)

    def insert(self, val):
        length = len(self.arr)
        self.size += 1
        if self.arr == []:
            self.arr[length:] = [val]
        else:
            temp = length
            self.arr[length:] = [val]
            self.arr[0], self.arr[temp] = self.arr[temp], self.arr[0]
        self.build_max_heap()

    def delete(self):
        if self.arr == []:
            return "Array Empty"
        deleted = self.arr[0]
        if len(self.arr) == 1:
            self.size -= 1
            return deleted
        last = self.arr[self.size - 1]
        self.arr[0] = last
        self.size -= 1
        self.build_max_heap()
        return 'Deleted:',deleted

    def search(self, val):
        for i in range(self.size):
            if self.arr[i] == val:
                return True
        return False

    def print(self):
        for i in range(0, self.size):
            print(self.arr[i])
        print("Size:",self.size)


max = maxheap()

print(max.delete())
max.print()
max.insert(3)
max.insert(2)
max.insert(8)
max.insert(9)
max.insert(1)
max.insert(7)
max.insert(19)
max.insert(6)
max.insert(22)
max.print()

print(max.delete())
max.print()
print(max.delete())
max.print()

print(max.search(2))
print(max.search(5))
print(max.search(222))
print(max.search(22))









