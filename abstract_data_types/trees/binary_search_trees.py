class TreeNode:
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
    
    def search(self, search_value, current_node=None):
        if current_node is None:
            current_node = self
        else:
            if current_node.value < search_value:
                if current_node.value is None:
                    return None
                self.left_child.search(search_value, current_node.right_child)
            elif current_node.value > search_value:
                if current_node.value is None:
                    return None
                self.right_child.search(search_value, current_node.left_child)
            else:
                return current_node