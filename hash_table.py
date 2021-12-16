class hash_table:
    def __init__(self, size):
        self.size = size
        self.arr = [None for i in range(self.size)]

    def hash(self, key):
        num = 0
        for char in key:
            num += ord(char)
        return num % self.size

    def insert(self, key, val):
        num = self.hash(key)
        self.arr[num] = val

    def retrieve(self, key):
        num = self.hash(key)
        print(self.arr[num])
        

h = hash_table(5)
h.insert("key1", 2203)
h.insert("key2", 1212)
h.insert("key3", 3010)
h.retrieve("key1")
h.retrieve("key2")
h.retrieve("key3")



        
