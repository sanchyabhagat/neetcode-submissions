class Solution:
    def rob(self, nums: List[int]) -> int:
        # basic houserobber
        # rob1, rob2, 0, 1 , 2
        # either we take rob2 or rob1 + n
        if len(nums) == 1:
                return nums[0]
        def houseRob(nums):
            rob1, rob2 = 0, 0
            
            for n in nums:
                tmp = max(rob2, n + rob1)
                rob1 = rob2
                rob2 = tmp
            
            return rob2
        
        return max(houseRob(nums[0:len(nums)-1]), houseRob(nums[1:len(nums)]))
                
        