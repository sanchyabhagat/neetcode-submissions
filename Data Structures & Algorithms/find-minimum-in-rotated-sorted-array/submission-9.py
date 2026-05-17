class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r = 0, len(nums)-1
               
        while l <= r:

             # already sorted
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
                
            m = (l + r) // 2

            res = min(res, nums[m])

            # This helps us find the right side to look for
            
            if nums[m] >= nums[l]:
                l = m + 1
            
            else:
                r = m - 1
        
        return res

        