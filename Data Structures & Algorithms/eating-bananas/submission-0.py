class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Our search area will be from 1 -> max value 
        l, r = 1, max(piles)

        # max possible eating rate will be the max element
        res = r

        while l <= r:
            k = (l + r) // 2
            totalTime = 0
            # calculate time for mid
            for p in piles:
                # total time to finish each pile and round up each time
               totalTime += math.ceil(p / k) 

            if totalTime <= h:
               res = min(k, res)
               r = k - 1 # update right pointer to find a new minumum potentially

            elif (totalTime > h):
                l = k + 1

        return res     
