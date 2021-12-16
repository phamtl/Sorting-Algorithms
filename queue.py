class Queue:
    def __init__(self, size):
        self.temp_arr = ["e"]
        self.size = size
        self.arr = self.temp_arr * self.size
        self.tail = 0
        self.head = 0

    def queue_empty(self):
        return self.head == self.tail
    def queue_full(self):
        return self.head == (self.tail + 1) or (self.head == 0 and self.tail == (len(self.arr)-1))

    def enqueue(self, x):
        if self.queue_full() == True:
            return "Queue Overflow"
        else:
            self.arr[self.tail] = x
            if self.tail == len(self.arr):
                self.tail = 0
            else:
                self.tail += 1

    def dequeue(self):
        if self.queue_empty() == True:
            return "Queue Underflow"
        else:
            removed = self.arr[self.head]
            self.arr[self.head] = 'e'
            if self.head == len(self.arr):
                self.head = 0
            else:
                self.head += 1
            return removed

q = Queue(10)

print(q.queue_empty())

print("enqueue")
def enq():
    for i in range(10):
        q.enqueue(i)
enq()

print("dequeue")
print(q.arr)
print('')

def deq():
    for i in range(10):
        q.dequeue()
deq()


import timeit
print(timeit.timeit(deq, number = 100000))






    
