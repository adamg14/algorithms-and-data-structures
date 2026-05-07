from abstract_data_types.linked_lists.linked_list_2 import Node, LinkedList
from typing import Optional


class DoubleNode(Node):
    def __init__(
            self,
            value,
            next_node: Optional[DoubleNode] = None,
            previous_node: Optional[DoubleNode] = None
            ):
        super().__init__(value, next_node)
        self.previous_node = previous_node
    
    def __str__(self) -> str:
        return str(self.value)


class DoubleLinkedList(LinkedList):
    def __init__(
            self,
            root_node: Optional[DoubleNode] = None, 
            last_node: Optional[DoubleNode] = None
            ):
        super().__init__(root_node)
        self.last_node = last_node
    
    def __str__(self):
        return f"""
    Root Node Value: {self.root_node}
    Last Node Value: {self.last_node}
"""
    

    def insertion_end(
            self,
            new_node: DoubleNode,
            index: Optional[int] = None
            ):
        # inserting into the end of the queue
        if self.root_node is None:
            self.root_node = new_node
            self.last_node = new_node
        else:
            prev_last_node = self.last_node
            prev_last_node.next_node = new_node
            new_node.previous_node = prev_last_node
            self.last_node = new_node
    
    def reverse_read(self):
        reverse_list = []
        if self.last_node is None:
            return None
        else:
            current_node = self.last_node
            while current_node is not None:
                reverse_list.append(current_node.value)
                current_node = current_node.previous_node
    
    # need to ovewrite the linked list methods
    #  that required extra functionality
    
    def remove_first(self):
        if self.root_node is None:
            # The linked list is empty
            return False
        elif self.root_node.next_node is None:
            # only one element in the linked list
            removed_node = self.root_node
            return removed_node.value
        else:
            # more than one element in the linked list
            removed_node = self.root_node
            self.root_node = self.root_node.next_node
            return removed_node.value
    
    

first_node = DoubleNode(1)
second_node = DoubleNode(2)
third_node = DoubleNode(3)
fourth_node = DoubleNode(4)

first_node.next_node = second_node

second_node.previous_node = first_node
second_node.next_node = third_node

third_node.previous_node = second_node
third_node.next_node = fourth_node

fourth_node.previous_node = third_node

