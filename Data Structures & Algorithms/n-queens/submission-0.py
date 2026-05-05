class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set() # track if col already has a queen
        posDia = set() # track r+c i.e. if positive diagnal already taken by another queen
        negDia = set() # track r-c i.e. if negative diagnal already taken by another queen

        # board start with "." nxn
        board = [["."] * n  for i in range(n)]

        res = []

        # main backtrack dfs that goes row by row
        def backtrack(r):
             # base condition
            if r == n:
                # copy each row to a string
                output = ["".join(row) for row in board]
                res.append(output)
                return
            
            # else continue
            for c in range(n):
                # Queen space invalid
                if c in cols or r+c in posDia or r-c in negDia:
                    continue
                
                cols.add(c)
                posDia.add(r+c)
                negDia.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                cols.remove(c)
                posDia.remove(r+c)
                negDia.remove(r-c)
                board[r][c] = "."
        
        backtrack(0)
        return res

        