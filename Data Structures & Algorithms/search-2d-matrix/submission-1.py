class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find target row
        # bbinary search on target row
        ROWS,COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS-1

        while top <= bot:
            mid = (top + bot) // 2

            if matrix[mid][0] > target:
                bot -= 1
            
            elif matrix[mid][-1] < target:
                top += 1
            
            else:
                break
        
        if top > bot:
            return False
        
        # if not, then we found the row!

        row = (top + bot) // 2

        l, r = 0, COLS-1

        while l <= r:
            m = (l+r) // 2

            if matrix[row][m] == target:
                return True
            
            elif matrix[row][m] > target:
                r = m-1
            
            else:
                l = m+1
        
        return False