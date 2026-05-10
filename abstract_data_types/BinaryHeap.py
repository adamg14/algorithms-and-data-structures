# Implementation of Binary max-heap tree
# wit the underlying structure being an array

def get_parent_index(index):
    return (index - 1) // 2

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
        self._bubble_up()
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
    

    def delete(self):
        if self.heap_length == 0:
            return None
        else:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            self.heap = self.heap[:-1]
            self.heap_length -= 1

            self._trickle_down()

    
    def _trickle_down(self):
        current_index = 0
        # only need to check for left child as if this condition
        # fails for left child it automatically fails for right child
        while get_left_child_index(current_index) < self.heap_length:
            left_child = get_left_child_index(current_index)
            right_child = get_right_child_index(current_index)

            if left_child <= (self.heap_length - 1) and (right_child <= self.heap_length - 1):
                if self.heap[left_child] >= self.heap[right_child]:
                    if self.heap[current_index] < self.heap[left_child]:
                        self.heap[current_index], self.heap[left_child] = self.heap[left_child], self.heap[current_index]
                        current_index = left_child
                    else:
                        break
                else:
                    if self.heap[current_index] < self.heap[right_child]:
                        self.heap[current_index], self.heap[right_child] = self.heap[right_child], self.heap[current_index]
                        current_index = right_child
                    else:
                        break
            
            elif left_child <= (self.heap_length - 1):
                if self.heap[current_index] < self.heap[left_child]:
                    self.heap[current_index], self.heap[left_child] = self.heap[left_child], self.heap[current_index]
                    current_index = left_child
                else:
                    break
            
            else:
                if self.heap[current_index] < self.heap[right_child]:
                        self.heap[current_index], self.heap[right_child] = self.heap[right_child], self.heap[current_index]
                        current_index = right_child
                else:
                    break


    
