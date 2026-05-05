class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curMax = 0
        i,j = 0, len(heights)-1

        while j>i:
            localMax = (j-i) * min(heights[j], heights[i])

            if (localMax > curMax):
                curMax = localMax
            
            if (heights[j] > heights[i]):
                i += 1
            else:
                j -= 1
        
        return curMax

        