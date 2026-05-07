from linked_list_2 import Node, LinkedList
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
    
    def __str(self) -> str:
        return str(self.value)


class DoubleLinkedList(Linked_List):
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
            new_node.previous_node = self.last_node
    
    
        