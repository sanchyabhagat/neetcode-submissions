class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            # prevent potential overflow in java or other bound languages. Not an issue in python
            m = l + ((r - l) // 2) 

            if nums[m] == target:
                return m
            
            elif nums[m] > target:
                r = m-1
            
            elif nums[m] < target:
                l = m+1
        
        return -1

        