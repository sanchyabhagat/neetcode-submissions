class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        out = [1] * len(nums)

        for i,n in enumerate(nums):
            # assign current prefix
            out[i] = prefix
            # update prefix
            prefix = n * prefix

        for i in range(len(nums)-1, -1, -1):
            # calculate the res first
            out[i] =  out[i] * postfix
            # then update postfix for current position
            postfix = nums[i] * postfix
        
        return out
            
