class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS = len(matrix), len(matrix[0])

        # initialize initialize binary serach to find target row
        top,bot = 0, ROWS-1

        while top <= bot:
            row = (top + bot) // 2
            if (target > matrix[row][-1]):
                top = row + 1
            
            elif(target < matrix[row][0]):
                bot = row - 1
            
            else:
                break
        
        ## if we're here - that means either the loop hit code ending condition 
        # or we found the target row
        if not (top <= bot):
            return False
        
        # Else we found our target row, do binary search
        row = (top + bot) // 2
        l,r = 0, len(matrix[row])
        while l <= r:
            mid = (l + r) // 2
            if (target == matrix[row][mid]):
                return True
            elif (target > matrix[row][mid]):
                l = mid + 1
            elif (target < matrix[row][mid]):
                r = mid - 1
        
        return False


        
        