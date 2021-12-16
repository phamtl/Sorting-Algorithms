class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        
class dictionary:
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
        node = self.arr[num]
        if node is None:
            self.arr[num] = Node(key, val)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, val)

    def search(self, key):
        num = self.hash(key)
        node = self.arr[num]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return "Cannot find"
        else:
            return node.val

    def delete(self, key):
        num = self.hash(key)
        node = self.arr[num]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return "Cannot delete"
        else:
            deleted = node.val
            node = None
            return deleted
    

d = dictionary(5)
d.insert("key1", 2203)
d.insert("key2", 3010)
d.insert("key4", 1212)
d.insert("key6", 3006)

print(d.search("key2"))
print(d.search("key6"))
print(d.search("keyc"))

print(d.delete("key4"))
print(d.delete("key1"))













        
