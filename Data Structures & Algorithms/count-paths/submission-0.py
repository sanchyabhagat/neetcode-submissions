class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        
        # last row is all 1s - only one possible path to right
        bottomRow = [1] * n
        for i in range(m-1): # ignore last row since all will be "1"
            # init current row - we will update this below
            newRow = [1] * n

            # all columns EXCEPT last, avoiding edge cases
            for j in range(n-2, -1, -1):
                # update with right and bottom result in row below -> "row"
                newRow[j] = newRow[j+1] + bottomRow[j]
            # update our bottom row to current
            bottomRow = newRow
        
        # at the end we want to return first element that has sum of everything
        return bottomRow[0]




      

        