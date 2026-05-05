class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            
            cur =  cur.children[c]
        cur.isWord = True
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res, visit = set(), set()
        ROWS, COLS = len(board), len(board[0])
        # initial empty Tree root node
        root = TrieNode()

        # build words in Trie
        for w in words:
            root.addWord(w)
        
        # backtrack each possible element while searching in Trie for valid words
        def dfs(r, c, node, word):
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r,c) in visit or board[r][c] not in node.children:
                return
            
            visit.add((r,c))
            # update node to the next valid child
            node = node.children[board[r][c]]
            # add to the word we're building
            word += board[r][c]

            # SOLUTION: Check for word being valid
            if node.isWord:
                res.add(word)
            
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)

            # reset backtrack
            visit.remove((r,c))
        
        # go through all possible boards elements
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return list(res)

        