class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n) time and space
        # prepare hashset for O(1) lookup
        numSet = set(nums)
        res = 0

        for n in nums:
            # find strat of a valid sewuence, example 1,2,3 -> 1 will have no left neighbor since no 0
            if n - 1 not in numSet:
                length = 0
                while n + length in numSet:
                    length += 1

                res = max(res, length)
        
        return res

        
