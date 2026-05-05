class Solution:
    def findMin(self, nums: List[int]) -> int:
        # initialize
        res = nums[0]
        l,r = 0, len(nums)-1

        # condition
        while l <= r:

            # exit condition, already sorted array, all unique values given
            if (nums[l] < nums[r]):
                res = min(res, nums[l])
                break;
            
            # get mid element
            m = (l + r) // 2

            res = min(res, nums[m])

            # update conditions for binary search
            if (nums[m] >= nums[l]):
                l = m + 1   # search right side
            
            else:
                r = m - 1    # search left side
            
        return res
        