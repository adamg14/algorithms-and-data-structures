# Python Linked List operation where Node class is decoupled from Linked List
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = None
    
    def has_next_node(self):
        return self.next_node is not None

    def __str__(self):
        return f"Node: {self.value}"

class LinkedList:
    def __init__(self, root_node):
        self.root_node = root_node
    
    def __str__(self):
        return f"Root node: {self.root_node.value}"
    
    def read(self):
        if self.root_node is None:
            return 0
        current_node = self.root_node
        while current_node is not None:
            print(current_node)
            current_node = current_node.next_node
        return 1


    def linked_list_as_array(self):
        return_array = []
        current_node = self.root_node
        while current_node is not None:
            return_array.append(current_node.value)
            current_node = current_node.next_node
        return return_array


    def find_value(self, value):
        current_node = self.root_node
        current_index = 0
        while current_node is not None:
            if current_node.value == value:
                return current_index
            else:
                current_node = current_node.next_node
                current_index += 1
        
        return -1

    

first_node = Node(1)
second_node = Node(2)
third_node = Node(3)
fourth_node = Node(4)

first_node.next_node = second_node
second_node.next_node = third_node
third_node.next_node = fourth_node

ll1 = LinkedList(first_node)
print(first_node.has_next_node())
print(second_node.has_next_node())

print(first_node)
print(second_node)
print(ll1)
print("Reading the Linked List: ")
print(ll1.read())
print("Returning the linked list as an array: ")
print(ll1.linked_list_as_array())
print(ll1.find_value(3))
print(ll1.find_value(5))
    
        