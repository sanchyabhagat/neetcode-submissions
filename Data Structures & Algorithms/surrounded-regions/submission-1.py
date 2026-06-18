class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # find unsurrounded "0" on the borders using for loop
        # find all "0"s connetced this way -> mark them as T
        # after dfs finishes for all ) nodes on the edges: 
        # mark all Ts as 0s
        # mark all 0s (surrounded confirmed) -> as X

        ROWS, COLS = len(board), len(board[0])

        def dfs(r,c):
            if r not in range(ROWS) or c not in range(COLS) or board[r][c] != "O":
                return
            
            # mark unsurrounded
            board[r][c] = "T"

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

            return
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS-1] or c in [0, COLS-1]):
                    dfs(r,c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
        

                

        