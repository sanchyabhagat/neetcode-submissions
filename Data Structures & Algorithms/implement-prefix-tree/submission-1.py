class TrieNode:
    def __init__(self):
        # children
        self.children = {}
        # marks if the end of a letter is a word
        self.isWord = False

class PrefixTree:

    def __init__(self):
        # init a root node
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            
            # move down the Trie to add our word
            cur = cur.children[c]
        # once w ereach the end mark it as the word
        cur.isWord = True


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return True
        
        