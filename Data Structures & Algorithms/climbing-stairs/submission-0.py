class Solution:
    def climbStairs(self, n: int) -> int:
        # pointer at n-1
        one = 1
        # pointer at n:
        two = 1

        # n-1 since "one" will reach 0th positionb first
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        
        return one
        