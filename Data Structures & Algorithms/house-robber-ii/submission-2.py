class Solution:
    def rob(self, nums: List[int]) -> int:
        # house robber 1 + circular arrangement
        # either we pick first to second last
        # or second to last

        if len(nums) == 1:
            return nums[0]

        def houseRob(nums):
            rob1, rob2 = 0, 0

            for n in nums:
                temp = max(rob2, rob1 + n)
                rob1 = rob2
                rob2 = temp
            
            return rob2
        
        return max(houseRob(nums[0:len(nums)-1]), houseRob(nums[1:len(nums)]))
        