# Python Linked List operation where Node class is decoupled from Linked List
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = None
    
    def has_child(self):
        return self.next_node is not None

    def __str__(self):
        return f"Node: {self.value}"

class LinkedList:
    def __init__(self, root_node):
        self.root_node = root_node
    
    def __str__(self):
        return f"Root node: {self.root_node.value}"
    

first_node = Node(1)
second_node = Node(2)
first_node.next = second_node

ll1 = LinkedList(first_node)
print(first_node.has_child())
print(second_node.has_child())

print(first_node)
print(second_node)
print(ll1)
    
    
        