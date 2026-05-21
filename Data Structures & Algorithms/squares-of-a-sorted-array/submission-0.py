class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, resIndex = 0, len(nums)-1, len(nums)-1
        res = [0] * len(nums)

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[resIndex] = nums[l] * nums[l]
                l += 1
                
            
            else:
                res[resIndex] = nums[r] * nums[r]
                r -= 1
            
            resIndex -= 1
        
        return res
        