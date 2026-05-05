class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        # Algo is O(n^2) better than 2^n

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                # valid increasing case
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        return max(LIS)
