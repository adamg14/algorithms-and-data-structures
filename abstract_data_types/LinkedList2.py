# Python Linked List operation where Node class is decoupled from Linked List
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = None
    
    def has_child(self):
        return self.next is not None

class LinkedList:
    def __init__(self, root_node):
        self.root_node = root_node
    
    
        