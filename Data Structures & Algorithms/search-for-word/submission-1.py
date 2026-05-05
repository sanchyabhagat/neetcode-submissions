class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            # base case
            if i == len(word):
                return True
            
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or board[r][c] != word[i]:
                return False
            
            visit.add((r,c))

            res = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)

            # reset visit after path has been explored so other paths can access it
            visit.remove((r,c))

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c, 0): return True

        return False        