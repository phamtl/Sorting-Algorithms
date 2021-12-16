class Binary_tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val is None:
            self.val = Binary_tree(val)
        else:
            if self.left is None:
                self.left = Binary_tree(val)
            else:
                self.right = Binary_tree(val)
                
    def print_tree(self):
      if self.left is not None:
         self.left.print_tree()
      print(self.val),
      if self.right is not None:
         self.right.print_tree()

        
b = Binary_tree(5)
b.insert(4)
b.insert(6)
b.insert(7)
b.print_tree()



        
        
