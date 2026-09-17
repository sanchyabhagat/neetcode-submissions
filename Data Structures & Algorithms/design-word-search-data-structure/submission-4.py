class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

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

        # this will have to be a recursive function due to "." requirement

        def dfs(j, root):
            cur = root
            
            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for node in cur.children.values():
                        if dfs(i+1, node):
                             return True
                    return False
                else:
                    # normal search
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
                
            return cur.word


        return dfs(0, self.root)    
        
