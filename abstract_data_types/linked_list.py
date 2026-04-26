class LinkedList:
    class Node:
        def __init__(self, value, next_node=None):
            self.value = value
            self.next_node = next_node
        
        def has_child(self):
            return self.next_node is not None

    def __init__(self, root_node=None):
        self.root = root_node
    
    
    def add(self, node: Node):
        """add a node at the end of a linked list"""
        if self.root is None:
            self.root = node
        else:
            curr = self.root
            while curr.has_child():
                curr = self.root.next_node
            
            curr.next_node = node
    
    def get_last(self) -> int:
        """return the last node of the linked list"""
        if self.root.next_node is None:
            return self.root.value
        else:
            curr = self.root
            while curr.has_child():
                curr = self.next_node
            
            return curr.value

    def remove(self, value):
        """a value is inputted
        the location of the """
        # case where the root node is the one to be deleted
        if self.root is None:
            return False
        if self.root.value == value:
            self.root = self.root.next_node
            return True
        else:
            curr = self.root
            while curr.has_child():
                if curr.next_node.value == value:
                    if curr.next_node.next_node is None:
                        curr.next_node = None
                        return True
                    else:
                        curr.next_node = curr.next_node.next_node
                        return True
                else:
                    curr = curr.next_node
            return False

            

    def __str__(self):
        """the string representation of the linked list"""
        values = ""
        if self.root is None:
            return "Empty Linked List"
        if self.root.next_node is None:
            return str(self.root.value)
        curr = self.root

        while curr.has_child():
            values += f"{str(curr.value)}, "
            curr = curr.next_node
        values += str(curr.value)
        return values
    
ll = LinkedList()
ll.add(LinkedList.Node(1))
ll.add(LinkedList.Node(2))
ll.add(LinkedList.Node(3))
print(ll)
ll.remove(2)
print(ll)
ll2 = ll = LinkedList()
ll2.add(LinkedList.Node(1))
print(ll2)
ll2.remove(1)
print(ll2)
ll3 = LinkedList()
ll3.add(LinkedList.Node(1))
ll3.add(LinkedList.Node(2))
ll3.add(LinkedList.Node(3))
print(ll3)
ll3.remove(3)
print(ll3)

ll4 = LinkedList()
ll4.add(LinkedList.Node(1))
ll4.add(LinkedList.Node(2))
ll4.add(LinkedList.Node(3))
print(ll4)
ll4.remove(1)
print(ll4)