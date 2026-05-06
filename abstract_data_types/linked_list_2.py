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

    def remove_duplicates(self):
        current_node = self.root_node
        while current_node is not None and current_node is not None:
            if current_node.value == current_node.next.val:
                current_node.next = current_node.next.next
            else:
                current_node.next
    
    def add_node(self, new_node, index=None):
        # index starts from element zero
        if index is not None:
            if index == 0:
                # the new element should be added
                # to the start of the linked list
                old_root_node = self.root_node
                self.root_node = new_node
                new_node.next_node = old_root_node
            else:
                current_node = self.root_node
                current_index = 0
                while current_index < (index - 1) and current_node is not None:
                    current_node = current_node.next_node
                    current_index += 1
                
                if current_node.has_next_node():
                    last_node = current_node.next_node
                    current_node.next_node = new_node
                    new_node.next_node = last_node
                else:
                    current_node.next_node = new_node
        else:
            # if index is None, it is an ordered array
            # so insertion needs to maintain order
            current_node = self.root_node
            inserted = False
            if current_node.value >= new_node.value:
                self.root_node = new_node
                self.root_node.next_node = current_node
                return 1
            while current_node is not None and current_node.value < new_node.value:
                if current_node.has_next_node():
                    current_node = current_node.next_node
                else:
                    current_node.next_node = new_node
                    inserted = True
                    break
            
            if inserted:
                return 1
            else:
                if current_node.has_next_node():
                    last_node = current_node.next_node
                    current_node.next_node = new_node
                    new_node.next_node = last_node
                    return 1
                else:
                    current_node.next_node = new_node
                    return 1

            

            


first_node = Node(1)
second_node = Node(2)
third_node = Node(3)
fourth_node = Node(4)

first_node.next_node = second_node
second_node.next_node = third_node
third_node.next_node = fourth_node

new_node = Node(5)
linked_list = LinkedList(first_node)
print(linked_list.linked_list_as_array())
linked_list.add_node(new_node)
print(linked_list.linked_list_as_array())

    
        