class TrieNode:
    def __init__(self):
        self.children = {}  # Child nodes, stored in a dictionary (can also use a list for limited alphabets)
        self.is_end_of_word = False  # Flag to indicate if the node marks the end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root node of the trie

    # Insert a word into the trie
    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # Create a new node if it doesn't exist
            node = node.children[char]
        node.is_end_of_word = True  # Mark the end of the word

    # Search for a word in the trie
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False  # If a character is not found, word doesn't exist
            node = node.children[char]
        return node.is_end_of_word  # Return true only if the node is the end of the word

    # Delete a word from the trie
    def delete(self, word: str):
        self._delete(self.root, word, 0)
        
    # Helper function for deletion (recursive)
    def _delete(self, node, word, index):
        if index == len(word):
            if not node.is_end_of_word:
                return False  # Word doesn't exist
            node.is_end_of_word = False  # Unmark the end of the word
            return len(node.children) == 0  # If no children, node can be deleted

        char = word[index]
        if char not in node.children:
            return False  # If a character doesn't exist, word is not in the trie

        # Recursively delete the character
        can_delete_child = self._delete(node.children[char], word, index + 1)

        if can_delete_child:
            del node.children[char]  # Delete the child node if it's no longer needed
            return len(node.children) == 0  # Return true if the current node has no other children

        return False  # If the node cannot be deleted, return False

# Create a Trie object
trie = Trie()

# Insert words
trie.insert("hello")
trie.insert("helium")
trie.insert("he")

# Search for words
print(trie.search("hello"))  # True
print(trie.search("helium"))  # True
print(trie.search("he"))  # True
print(trie.search("hell"))  # False

# Delete a word
trie.delete("helium")
print(trie.search("helium"))  # False

# Try to delete a non-existing word
trie.delete("world")  # No effect, as "world" doesn't exist


# Complexity Analysis
# Insert: O(m), where m is the length of the word being inserted. 
# We perform one operation for each character.
# Search: O(m), where m is the length of the word being searched. 
# We check each character of the word in the trie.
# Delete: O(m), where m is the length of the word being deleted. 
# In the worst case, we may have to traverse the entire word and possibly delete nodes.