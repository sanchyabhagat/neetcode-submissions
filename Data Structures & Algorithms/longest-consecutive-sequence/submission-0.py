class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        self.numSet = set(nums)
        res = 0

        for n in nums:
            if n-1 in self.numSet:
                continue
            
            res = max(res, self.getLongestSequence(n))
        
        return res

    def getLongestSequence(self, n):
        res = 0
        while n in self.numSet:
            res += 1
            n = n+1
            
        return res

            

        