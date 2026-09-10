class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # need to go through all possible r, c with current word[i] in dfs
        # maintain visit set per branch then reset it after path is visited

        visit = set()
        rows, cols = len(board), len(board[0])

        def dfs(r, c , i):
            # base case
            if i == len(word):
                return True
            
            # boundary
            if (r not in range(rows) or c not in range(cols) or board[r][c] != word[i] or (r,c) in visit):
                return

            visit.add((r,c))
            res = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
            
            # remove from visit
            visit.remove((r,c))

            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True
        
        return False
        