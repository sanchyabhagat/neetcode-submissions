class TrieNode:
    def __init__(self):
        self.children = {} # stores trieNode as chidren chars values
        self.word = False  # Mark as end of word 

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True        

    def search(self, word: str) -> bool:
        # j is the start of subroot index
        # in case we hit a "." this will make sure we traverse all children paths
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for node in cur.children.values():
                        if dfs(i+1, node):
                            return True
                    return False # return false if ALLL possible paths didnt result in True
                
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word # return if end of the chars is a valid inserted word in trie
        
        return dfs(0, self.root)
        
