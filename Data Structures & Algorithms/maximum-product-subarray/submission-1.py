class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # not 0 since that may break our base case
        res = max(nums)

        minPro = 1
        maxPro = 1
        for n in nums:
            # edge case if element is zero
            if n == 0:
                minPro = 1
                maxPro = 1
                continue
            # since we'll change curMax soon
            tmp = n * maxPro

            maxPro = max(n * maxPro, n * minPro, n)
            minPro = min(tmp, n * minPro, n)
            res = max(res, maxPro) 
        
        return res
        