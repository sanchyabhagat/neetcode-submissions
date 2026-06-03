class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use floyd's algo to find the intersection point
        # i.e. start of the cyintersectioncle == slow1
        # then start a slow pointer from beginning 
        # Using algebra -> when old(slow1) and new slow meet,
        # it will be at the duplicate/cycle start
        # This problem is just memorization

        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            # intersection point slow1
            if slow == fast:
                break
        
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                break
        
        # return the duplicate not the index
        return slow




        