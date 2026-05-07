from abstract_data_types.linked_lists.double_linked_list import DoubleNode, DoubleLinkedList
from abstract_data_types.linked_lists.linked_list_2 import Do
from typing import Optional
# Implementation (LiLO) Queue using nodes as elements
# using Doubly Linked Lists
# Property of queues can only remove from the front 
# and add at the end


class Queue(DoubleLinkedList):
    def __init__(
            self,
            root_node: Optional[DoubleNode] = None, 
            last_node: Optional[DoubleNode] = None
    ):
        # initialise the Queue
        super().__init__(root_node, last_node)
        self.queue = DoubleLinkedList()
        
    
    def enqueue(self, element: DoubleNode):
        self.queue.insert_end(element)
        return element
    

    def dequeue(self):
        return self.queue.remove_first()