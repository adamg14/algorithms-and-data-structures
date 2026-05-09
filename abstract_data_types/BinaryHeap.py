# Implementation of Binary max-heap tree
# wit the underlying structure being an array

def get_parent_index(index):
    return (index - 1) * 2

def get_left_child_index(index):
        return (index * 2) + 1
    

def get_right_child_index(index):
    return (index * 2) + 2


class BinaryHeapNode:
    def __init__(self):
        self.heap = []
        self.heap_length = 0


    def insertion(self, value):
        # add the new value to the end of the array (heap)
        self.heap_length += 1
        self.heap.append(value)
        # call the bubble up method
        # to compare the newly added value to the decendants
        # to ensure the heap property is maintained
        self._bubble_up(value)
        return value

    def _bubble_up(self):
        # start at the end of the list
        current_index = self.heap_length - 1
        while current_index > 0:
            parent_index = get_parent_index(current_index)
            if self.heap[parent_index] < self.heap[current_index]:
                self.heap[parent_index], self.heap[current_index] = self.heap[current_index], self.heap[parent_index]
                current_index = parent_index
            else:
                # the value at the current_index (the newly added value is in the correct position)
                break
    

    def get_heap(self):
        return self.heap


    def get_heap_length(self):
        return len(self.heap)
    

    def pop_heap(self):
        pop_element = self.heap[0]
        self.heap = self.heap[1:]
        self.heap_length -= 1

    def deletion(self):
        # always delete the element with the 
        # highest priority (the first element)
        if len(self.heap) == 0:
            return None
        else:
            pass
    
