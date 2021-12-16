class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
        
class AVL:
    def Height(self, node):
        if node is None:
            return 0
        else:
            return node.height
        
    def balance_state(self, node):
        if node is None:
            return 0
        else:
            return self.Height(node.left) - self.Height(node.right)

    def compare(self, var1, var2):
        if var1 > var2:
            return var1
        else:
            return var2
        
    def left_rotate(self, node):
        y = node.right
        temp = y.left
        y.left = node
        node.right = temp
        node.height = 1 + self.compare(self.Height(node.left), self.Height(node.right))
        y.height = 1 + self.compare(self.Height(y.left), self.Height(y.right))
        
    def right_rotate(self, node):
        y = node.left
        temp = y.right
        y.right = node
        node.left = temp
        node.height = 1 + self.compare(self.Height(node.left), self.Height(node.right))
        y.height = 1 + self.compare(self.Height(y.left), self.Height(y.right))
        
    def balance(self, node, val):
        bs = self.balance_state(node)
        if bs > 1 and node.left is not None:
            if val < node.left.val: #LL
                self.right_rotate(node)
            elif val > node.left.val: #LR
                self.left_rotate(node.left)
                self.right_rotate(node)
        if bs < -1 and node.right is not None:
            if val > node.right.val: #RR
                self.left_rotate(node)
            elif val < node.right.val: #RL
                self.right_rotate(node.right)
                self.left_rotate(node)

    def insert(self, root, val):
        if root is None:
            root = Node(val)
        else:
            if val < root.val:
                root.left = self.insert(root.left, val)
            else:
                root.right = self.insert(root.right, val)

        root.height = 1 + self.compare(self.Height(root.left), self.Height(root.right))
        self.balance(root, val)
        return root

    def search(self, root, val):
        if root.val == val:
            return True
        elif root.val > val and root.left is not None:
            return self.search(root.left, val)
        elif root.val < val and root.right is not None:
            return self.search(root.right, val)
        return False

    def preorder(self, root):
        if root is not None:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

import timeit
avl = AVL()
#def avl_insert():
root = None
for i in range(1000):
    root = avl.insert(root, i)

def avl_search():
    print(avl.search(root, 1022))
    print(avl.search(root, 0))
    print(avl.search(root, 2000))
    print(avl.search(root, 723))
    print(avl.search(root, 999))
#print(timeit.timeit(avl_insert, number=1))
print(timeit.timeit(avl_search, number=1))










                    
