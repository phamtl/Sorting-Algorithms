class Stack:
    def __init__(self, size):
        self.temp_arr = ["e"]
        self.size = size
        self.arr = self.temp_arr * self.size
        self.top = -1

    def stack_empty(self):
        return self.top == -1
    def stack_full(self):
        return (self.top+1) == len(self.arr)
    
    def push(self, x):
        if self.stack_full():
            return "Stack Overflow"
        else:
            self.top += 1
            self.arr[self.top] = x

    def pop(self):
        if self.stack_empty() == True:
            return "Stack Underflow"
        else:
            popped = self.arr[self.top]
            self.arr[self.top] = 'e'
            self.top -= 1
            return popped

    def peek(self):
        if self.stack_empty():
            return "Stack Underflow"
        else:
            return self.arr[self.top]

s = Stack(10)

print(s.stack_empty())
def pus():
    for i in range(10):
        s.push(i)
pus()
print(s.arr)

print(s.peek())
print(s.arr)

def popp():
    for i in range(10):
        s.pop()
popp()
print(s.arr)

import timeit
print(timeit.timeit(pus, number=100000))
print(timeit.timeit(popp, number=100000))
