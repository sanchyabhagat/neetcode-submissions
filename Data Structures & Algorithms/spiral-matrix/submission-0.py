class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        out = []
        rows, cols = len(matrix), len(matrix[0])

        dirs = [0, 1, 0, -1, 0]
        k = 0
        r, c = 0, 0
        while True:
            if len(out) == rows * cols:
                return out
            
            out.append(matrix[r][c])
            matrix[r][c] = None
            newr, newc = r + dirs[k], c + dirs[k + 1]
            if newr not in range(rows) or newc not in range(cols) or matrix[newr][newc] == None:
                # move clockwise
                k = (k+1) % 4
            
            # switch new dirs potentially
            r, c = r + dirs[k], c + dirs[k + 1]
        