class Solution:
    def trap(self, height: List[int]) -> int:
        maxl, maxr = 0,0
        l,r, = 0, len(height)-1
        res = 0

        while l<=r:
            # move left since it's lower, we need the min out of two
            if maxl <= maxr:
                if maxl - height[l] > 0:
                    res += maxl - height[l]
                maxl = max(maxl, height[l])
                l = l+1
            
            else:
                if maxr - height[r] > 0:
                    res += maxr - height[r]
                
                maxr = max(maxr, height[r])
                r = r-1
        
        return res



        