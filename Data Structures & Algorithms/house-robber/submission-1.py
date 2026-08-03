class Solution:
    def rob(self, nums: List[int]) -> int:
        # cannot rob two consecutive houses
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(rob2, rob1 + n)
            rob1 = rob2
            rob2 = temp
        
        return rob2

        