class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        row, col = [False] * ROWS, [False] * COLS

        # find 0s
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    row[r] = True
                    col[c] = True
        
        # now convert
        for r in range(ROWS):
            for c in range(COLS):
                if row[r] or col[c]:
                    matrix[r][c] = 0
        
        
        