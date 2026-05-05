class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # add a zero since last cost will always be zero sicne we reached the end
        cost.append(0)

        # loop from the back
        for i in range(len(cost)-3, -1 , -1):
            cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])
        
        # finall return min of starting at 0 or 1
        return min(cost[0], cost[1])
        