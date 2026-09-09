class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums)-1
        # 3,4,5,6,1,2 -> find 1
        # 6,1,2,3,4,5 -> find 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            # left sorted 
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    # means we are out of this half's range
                    l = m+1
                else:
                    # means we are on the money!
                    r = m-1
            
            # right sorted
            else:
                if target > nums[r] or target < nums[m]:
                    # need to go left
                    r = m-1
                else:
                    l = m+1
        
        return -1
        