class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        maxPro = 1
        minPro = 1

        for n in nums:
            if n == 0:
                # base case reset max and min
                maxPro = 1
                minPro = 1
            
            # get current max
            tmp = maxPro * n

            maxPro = max(tmp, minPro*n, n)
            minPro = min(tmp, minPro*n, n)

            res = max(res, maxPro)
        
        return res
        