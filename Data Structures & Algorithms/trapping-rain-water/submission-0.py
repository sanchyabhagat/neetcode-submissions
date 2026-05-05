class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]
        totalWater = 0
        if not height:
            return 0
        
        while l < r:
            if  leftMax < rightMax:
                curWater = leftMax - height[l]
                if curWater > 0:
                    totalWater += curWater
                l = l+1
                leftMax = max(leftMax, height[l])

            else:
                curWater = rightMax - height[r]
                if curWater > 0:
                    totalWater += curWater
                r = r-1
                rightMax = max(rightMax, height[r])
        
        return totalWater
        