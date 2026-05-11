class TrieNode:
    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()
    

    def search(self, word):
        # O(K) = K is the length of the search word
        # start at the root node
        current_node = self.root

        # iterate over the characters in of the word
        for char in word:
            if current_node.get(char):
                current_node = current_node.children[char]
            else:
                # the word is not present in the Trie
                return None
        
        return current_node