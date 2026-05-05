class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        def houseRob(tempNumb):
            rob1, rob2 = 0, 0
            for n in tempNumb:
                temp = max(rob2, rob1 + n)
                rob1 = rob2
                rob2 = temp
        
            return rob2
        
        arr1 = nums[0:len(nums)-1]
        arr2 = nums[1: len(nums)]

        return max(houseRob(arr1), houseRob(arr2) )

        