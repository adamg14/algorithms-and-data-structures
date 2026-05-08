from typing import Optional

class TreeNode:
    def __init__(
            self,
            value,
            left_child: Optional[TreeNode] = None,
            right_child: Optional[TreeNode] = None
            ):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
    
    def __str__(self) -> str:
        return f"Tree Node({self.value})"


class BinarySearchTree:
    def __init__(self, root_node: Optional[TreeNode]=None):
        self.root_node = root_node
    
    def __str__(self) -> str: 
        return f"Binary Search Tree Root Node Value: {self.root_node.value}"
    

    def insert(self, new_node: TreeNode):
        if self.root_node is None:
            self.root_node = new_node
        else:
           self._insert(self.root_node, new_node)
    

    def _insert(self, current_node, new_node):
        if current_node.value > new_node.value:
            if current_node.left_child is None:
                current_node.left_child = new_node
                return new_node
            else:
                self._insert(current_node.left_child, new_node)
        else:
            if current_node.right_child is None:
                current_node.right_child = new_node
            else:
                self._insert(current_node=current_node.right_child)
    

    def search(self, search_value):
        if self.root_node == None:
            return None
        else:
            return self._search(self.root_node, search_value)
    

    def _search(self, current_node, search_value):
        if current_node.value == search_value:
                return current_node
        elif current_node.value > search_value:
            # search the left child
            if current_node.left_child is None:
                return None
            else:
                return self._search(current_node.left_child, search_value)
        else:
            # search the right child
            if current_node.right_child is None:
                return None
            else:
                return self._search(current_node.right_child, search_value)
            
    
    def traverse(self):
        result = []
        self._traverse(self.root_node, result)
        return result
    

    def _traverse(self, node, bst_array=[]):
        # go through all the elements in the BST
        # return the values as an array
        # uses recursion + memoization
        if node is None:
            # exit that recursive call
            return None
        self._traverse(node.left_child, bst_array)
        bst_array.append(node.value)
        self._traverse(node.right_child, bst_array)
        
        return bst_array
        

bst = BinarySearchTree()
bst.insert(TreeNode(5))
bst.insert(TreeNode(3))
bst.insert(TreeNode(7))
bst.insert(TreeNode(2))
print(bst.search(7))
print(bst.search(2))
print(bst.search(8))

print(bst.traverse())