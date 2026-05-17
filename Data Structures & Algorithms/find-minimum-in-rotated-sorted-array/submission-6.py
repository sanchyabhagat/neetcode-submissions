class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r = 0, len(nums)-1

        # already sorted
        if nums[l] <= nums[r]:
            return nums[l]
        
        while l <= r:
            m = (l + r) // 2

            res = min(res, nums[m])

            # search right side for smaller
            if nums[m] >= nums[0]:
                l = m + 1
            
            else:
                r = m - 1
        
        return res

        