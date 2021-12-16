class node:
    def __init__(self, key):
        self.key = key
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def insert_head(self, key):
        new_node = node(key)
        new_node.next = self.head
        self.head = new_node

    def insert_mid(self, key, value_before):
        node_look = self.head
        while node_look is not None:
            if value_before == node_look.key:
                break
            node_look = node_look.next
            
        if node_look is None:
            print("Cannot insert node")
            return
        new_node = node(key)
        new_node.next = node_look.next
        node_look.next = new_node

    def insert_end(self, key):
        new_node = node(key)
        if self.head is None:
            self.head = new_node
        else:
            node_look = self.head
            while node_look.next is not None:
                node_look = node_look.next
                
            node_look.next = new_node

    def delete_head(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            self.head = self.head.next

    def delete_mid(self, value):
        if self.head is None:
            print("Linked List is empty")
        else:
            if value == self.head.key:
                self.head = self.head.next
            else:
                node_look = self.head
                while node_look.next is not None:
                    if value == node_look.next.key:
                        break
                    node_look = node_look.next
                if node_look.next is None:
                    print("Cannot delete node")
                else:
                    node_look.next = node_look.next.next

    def delete_end(self):
        if self.head is None:
            print("Linked List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            node_look = self.head
            while node_look.next.next is not None:
                node_look.next
            node_look.next = None

    def search(self, value):
        node_look = self.head
        if node_look is None:
            print("Linked List is empty")
        else:
            while node_look is not None:
                if node_look.key == value:
                    return "Found"
                node_look = node_look.next
            return "Not found"
        
    def print(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            i = self.head
            while i is not None:
                print(i.key)
                i = i.next

ll = linked_list()
ll.insert_head(1)
ll.print()
print('')

ll.insert_head(3)
ll.print()
print('')

ll.insert_mid(2, 3)
ll.print()
print('')

ll.insert_end(5)
ll.print()
print('')

print(ll.search(3))
print(ll.search(8))

ll.delete_head()
ll.print()
print('')

ll.delete_mid(1)
ll.print()
print('')

ll.delete_end()
ll.print()













                  
