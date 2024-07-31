class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def visualize(self, node=None, level=0):
        if node is None:
            node = self.root
        for char, child in node.children.items():
            print(' ' * level * 4 + char)
            self.visualize(child, level + 1)
        if node.is_end_of_word:
            print(' ' * level * 4 + '(end of word)')
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    

trie = Trie()
trie.insert("cat")
trie.insert("car")
trie.visualize()