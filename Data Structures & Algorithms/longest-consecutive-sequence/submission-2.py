class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        res = 0

        for n in nums:
            if n - 1 not in numSet:
                len = 0
                while n+len in numSet:
                    len += 1
                res = max(res, len)
        
        return res
        