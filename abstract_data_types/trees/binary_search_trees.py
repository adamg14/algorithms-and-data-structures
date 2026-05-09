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
        # in order traversal
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
        
    def greatest_number(self):
        if self.root_node is None:
            return None
        else:
            current_node = self.root_node
            while current_node is not None:
                current_node = current_node.right_child 
            
            return current_node
    
    def array_bst(self, input_array: list):
        # this function takes an array as an input
        # and returns the array as a binary tree
        bst = BinarySearchTree()

        for element in input_array:
            bst.insert(TreeNode(element))
        
        return bst
    

    def deletion(self, value_to_delete, node=self.root):
        # base case
        # hit the bottom of the tree and the parent node
        # has no children
        if node is None:
            return None
        
        elif value_to_delete < node.value:
            node.left_child = self.deletion(value_to_delete, node.left_child)

            # return the current node
            # to be used as the new value of its parent's left or right child
            return node
        
        elif value_to_delete > node.value:
            node.right_child = self.deletion(value_to_delete, node.right_child)

            return node
        else:
            # value_to_delete == node.value
            
            # if the current node has no left children
            # delete it by returning the right child
            # to be the parent's new sub tree
            if node.left_child is None:
                return node.right_child
            elif node.right_child is None:
                return node.left_child
            else:
                # the current node has two children
                # delete the node by calling the lift function
                node.right_child = self.lift(node.right_child, node)

    def lift(self, node, node_to_delete):
        if node.left_child:
            # continously go to the left child to 
            # find the least of the numbers greater than the 
            # node being deleted (successor node)
            node.left_child = self.lift(node.left_child, node)
        
        # at this point there are no more chains of left children
        # therefore we have reached our successor node
        else:
            node_to_delete.value = node.value
            # return just the right child as the successor
            # will never have a left child
            # so the left child will be taken over from the deleted node
            return node.right_child


        

        


bst = BinarySearchTree()
bst.insert(TreeNode(5))
bst.insert(TreeNode(3))
bst.insert(TreeNode(7))
bst.insert(TreeNode(2))
print(bst.search(7))
print(bst.search(2))
print(bst.search(8))

print(bst.traverse())
print(bst.greatest_number())

bst_conversion = BinarySearchTree()
array_to_bst = bst_conversion.array_bst([5, 3, 7, 2])
print(array_to_bst)