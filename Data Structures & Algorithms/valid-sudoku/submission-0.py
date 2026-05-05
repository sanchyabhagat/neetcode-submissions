class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # set for col, row, and square
        # square is tricky since you need weird mod //
        # r // 3, c // 3 -> maps to 9 unique squares on the board

        rows, cols, squares = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c] 
                if val == ".":
                    continue
                
                if val in rows[r] or val in cols[c] or  val in squares[r // 3, c // 3]:
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                squares[r // 3,c // 3].add(val)
        
        return True
        