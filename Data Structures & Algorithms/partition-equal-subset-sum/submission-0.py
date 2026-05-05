class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # track possible sums in a set at anypoint
        # target will be half of toal sum == sum(nums) // 2
        # if target cannot be divided by 2, we return false
        if sum(nums) % 2 == 1:
            return False
        
        target = sum(nums) // 2

        dp = set()
        # Default, sum of not pickign anything at first
        dp.add(0)

        for i in range(len(nums)-1, -1, -1):
            dpClone = set()
            for t in dp:
                if nums[i] + t == target:
                    return True
                
                dpClone.add(nums[i] + t)
                dpClone.add(t)
            dp = dpClone
        
        if target in dp:
            return True
        
        return False
        